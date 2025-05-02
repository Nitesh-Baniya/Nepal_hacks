def evaluate_retrieval(query, retrieved_passages, relevance_scores, expected_concept):
    """
    Evaluate the retrieval performance

    Args:
        query: The user's question
        retrieved_passages: Retrieved passages
        relevance_scores: Similarity scores
        expected_concept: The expected concept that should be retrieved

    Returns:
        Evaluation metrics
    """
    # Check if the expected concept is in any of the retrieved passages
    found = any(expected_concept.lower() in passage.lower() for passage in retrieved_passages)

    # Calculate Mean Reciprocal Rank (MRR)
    rank = None
    for i, passage in enumerate(retrieved_passages):
        if expected_concept.lower() in passage.lower():
            rank = i + 1
            break

    mrr = 1 / rank if rank else 0

    # Calculate precision@k
    relevant_count = sum(1 for passage in retrieved_passages if expected_concept.lower() in passage.lower())
    precision_at_k = relevant_count / len(retrieved_passages)

    return {
        "found": found,
        "rank": rank,
        "mrr": mrr,
        "precision_at_k": precision_at_k,
        "top_relevance_score": max(relevance_scores) if relevance_scores else 0
    }
