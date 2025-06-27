
def eval_retrieval(queries, ground_truth, k):
    """
    Main evaluation function for drug crimes as specified in requirements

    Args:
        queries: List of drug crime evaluation queries
        ground_truth: List of relevant drug crime case IDs for each query
        k: Number of top cases to evaluate

    Returns:
        dict: Evaluation metrics (accuracy, precision, recall, f1_score)
    """
    # Load drug crime components
    import pandas as pd
    import numpy as np
    import joblib
    from sklearn.metrics.pairwise import cosine_similarity
    import re
    
    # Load drug crime data
    df = pd.read_csv('/content/drive/MyDrive/data/processed/drug_crime_cases_with_classification.csv')
    tfidf_vectorizer = joblib.load('/content/drive/MyDrive/models/drug_tfidf_vectorizer.pkl')
    tfidf_matrix = np.load('/content/drive/MyDrive/models/drug_tfidf_matrix.npy')
    
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
    
    def retrieve_drug_cases(query, k):
        processed_query = clean_text_for_drug_cases(query)
        query_vector = tfidf_vectorizer.transform([processed_query])
        similarities = cosine_similarity(query_vector, tfidf_matrix).flatten()
        top_k_indices = similarities.argsort()[-k:][::-1]
        
        case_ids = []
        for idx in top_k_indices:
            case_id = df.iloc[idx].get('case_id', f"drug_case_{idx+1:03d}")
            case_ids.append(case_id)
        return case_ids

    # Loop through each query and calculate metrics
    all_metrics = []

    for i, query in enumerate(queries):
        retrieved = retrieve_drug_cases(query, k)
        gt = ground_truth[i] if i < len(ground_truth) else []

        # Calculate metrics for this query
        retrieved_set = set(retrieved[:k])
        gt_set = set(gt[:k])

        tp = len(retrieved_set.intersection(gt_set))
        fp = len(retrieved_set - gt_set)
        fn = len(gt_set - retrieved_set)

        precision = tp / (tp + fp) if (tp + fp) > 0 else 0
        recall = tp / (tp + fn) if (tp + fn) > 0 else 0
        f1 = 2 * precision * recall / (precision + recall) if (precision + recall) > 0 else 0

        all_metrics.append({
            'precision': precision,
            'recall': recall,
            'f1_score': f1
        })

    # Return average metrics
    return {
        'precision': sum(m['precision'] for m in all_metrics) / len(all_metrics),
        'recall': sum(m['recall'] for m in all_metrics) / len(all_metrics),
        'f1_score': sum(m['f1_score'] for m in all_metrics) / len(all_metrics)
    }
