def evaluate_retrieval(query, retrieved, scores, expected):
    found = any(expected.lower() in r.lower() for r in retrieved)
    rank = next(
        (i + 1 for i, r in enumerate(retrieved) if expected.lower() in r.lower()), None
    )
    mrr = 1 / rank if rank else 0
    precision = sum(expected.lower() in r.lower() for r in retrieved) / len(retrieved)
    return {
        "found": found,
        "rank": rank,
        "mrr": mrr,
        "precision_at_k": precision,
        "top_score": max(scores),
    }
