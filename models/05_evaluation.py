
def eval_retrieval(queries, ground_truth, k):
    """
    Main evaluation function as specified in requirements
    
    Args:
        queries: List of evaluation queries
        ground_truth: List of relevant case IDs for each query
        k: Number of top cases to evaluate
    
    Returns:
        dict: Evaluation metrics (accuracy, precision, recall, f1_score)
    """
    # Implementation here matches the full evaluation above
    # This is the simplified version for the requirement
    
    # Loop through each query and calculate metrics
    all_metrics = []
    
    for i, query in enumerate(queries):
        retrieved = retrieve(query, k)
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
