
import pandas as pd
import numpy as np
import joblib
from sklearn.metrics.pairwise import cosine_similarity
import re
from collections import Counter

def predict_outcome(query: str) -> str:
    """
    Main prediction function as required for drug crime cases

    Args:
        query (str): New case description

    Returns:
        str: Predicted solution
    """
    # Load components - CORRECTED for drug crimes
    df = pd.read_csv('/content/drive/MyDrive/data/processed/drug_crime_cases_with_classification.csv')
    tfidf_vectorizer = joblib.load('/content/drive/MyDrive/models/drug_tfidf_vectorizer.pkl')
    tfidf_matrix = np.load('/content/drive/MyDrive/models/drug_tfidf_matrix.npy')

    # CORRECTED: Clean query using same method as case retrieval
    def clean_text_for_drug_cases(text):
        if pd.isna(text):
            return ""
        text = str(text).lower()
        text = re.sub(r'[^\w\s]', ' ', text)
        text = re.sub(r'\s+', ' ', text)
        
        stopwords = ['dan', 'atau', 'yang', 'untuk', 'dari', 'dengan', 'pada',
                    'dalam', 'ke', 'di', 'adalah', 'oleh', 'akan', 'telah', 'sudah',
                    'ini', 'itu', 'tidak', 'ada', 'juga', 'dapat', 'bisa', 'harus',
                    'maka', 'saja', 'hanya', 'masih', 'sebuah', 'satu', 'dua',
                    'bahwa', 'tersebut', 'sebagai', 'atas', 'karena', 'sehingga']
        
        drug_terms = ['uud', 'kuhp', 'uu', 'pp', 'thc', 'mdma']
        words = text.split()
        words = [word for word in words if (len(word) > 2 or word in drug_terms) and word not in stopwords]
        return ' '.join(words)

    # Get similar cases
    processed_query = clean_text_for_drug_cases(query)
    query_vector = tfidf_vectorizer.transform([processed_query])
    similarities = cosine_similarity(query_vector, tfidf_matrix).flatten()
    top_5_indices = similarities.argsort()[-5:][::-1]

    # Extract solutions from similar cases - ENHANCED for drug crimes
    solutions = []
    for idx in top_5_indices:
        case_data = df.iloc[idx]
        
        # Try multiple columns for punishment info
        punishment = None
        if pd.notna(case_data.get('jenis_hukuman')):
            punishment = str(case_data['jenis_hukuman'])
        elif pd.notna(case_data.get('status_putusan')):
            punishment = str(case_data['status_putusan'])
        
        if punishment:
            solutions.append(punishment)

    # Majority vote
    if solutions:
        most_common = Counter(solutions).most_common(1)[0][0]
        return most_common
    else:
        return "pidana penjara"  # Default prediction for drug crimes
