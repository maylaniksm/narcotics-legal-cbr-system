
def retrieve(query: str, k: int = 5) -> list:
    """
    Retrieve top-k most similar cases for a given query
    
    Args:
        query (str): Search query
        k (int): Number of cases to retrieve
    
    Returns:
        list: List of case_id strings
    """
    # Load models and vectorizers
    import joblib
    import numpy as np
    import pandas as pd
    from sklearn.metrics.pairwise import cosine_similarity
    import re
    
    # Load saved components
    tfidf_vectorizer = joblib.load('/content/drive/MyDrive/models/tfidf_vectorizer.pkl')
    tfidf_matrix = np.load('/content/drive/MyDrive/models/tfidf_matrix.npy')
    df = pd.read_csv('/content/drive/MyDrive/data/processed/cases_with_classification.csv')
    
    def clean_text_for_tfidf(text):
        """Clean text for TF-IDF processing"""
        if pd.isna(text):
            return ""
        
        text = str(text).lower()
        text = re.sub(r'[^\w\s]', ' ', text)
        text = re.sub(r'\s+', ' ', text)
        
        stopwords = ['dan', 'atau', 'yang', 'untuk', 'dari', 'dengan', 'pada', 
                    'dalam', 'ke', 'di', 'adalah', 'oleh', 'akan', 'telah', 'sudah',
                    'ini', 'itu', 'tidak', 'ada', 'juga', 'dapat', 'bisa', 'harus',
                    'maka', 'saja', 'hanya', 'masih', 'sebuah', 'satu', 'dua']
        
        words = text.split()
        words = [word for word in words if word not in stopwords and len(word) > 2]
        return ' '.join(words)
    
    # Process query
    processed_query = clean_text_for_tfidf(query)
    query_vector = tfidf_vectorizer.transform([processed_query])
    
    # Calculate similarities
    similarities = cosine_similarity(query_vector, tfidf_matrix).flatten()
    
    # Get top-k indices
    top_k_indices = similarities.argsort()[-k:][::-1]
    
    # Return case IDs
    case_ids = []
    for idx in top_k_indices:
        case_id = df.iloc[idx].get('case_id', f"case_{idx+1:03d}")
        case_ids.append(case_id)
    
    return case_ids
