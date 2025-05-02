from sentence_transformers import SentenceTransformer

embeddings = model.encode(df["Content"].tolist())


def create_embeddings(df):
    """Create embeddings for all descriptions in the DataFrame"""

    model = SentenceTransformer("all-MiniLM-L6-v2")

    df["Content"] = df["Concept"] + ": " + df["Description"]

    print(f"Created {len(embeddings)} embeddings of dimension {embeddings[0].shape[0]}")
    return embeddings


def retrieve_relevant_context(query, df, embeddings, top_k=3):
    """
    Retrieve the most relevant context passages for a given query

    Args:
        query: The user's question
        df: DataFrame containing our knowledge base
        embeddings: Pre-computed embeddings for each row in df
        top_k: Number of most relevant passages to retrieve

    Returns:
        List of relevant passages
    """
    query_embedding = model.encode([query])[0]

    similarities = cosine_similarity([query_embedding], embeddings)[0]

    top_indices = np.argsort(similarities)[-top_k:][::-1]

    relevant_passages = df.iloc[top_indices]["Content"].tolist()
    relevance_scores = similarities[top_indices]

    print("\n=== Retrieval Results ===")
    for i, (passage, score) in enumerate(zip(relevant_passages, relevance_scores)):
        print(f"Result {i+1} [Similarity: {score:.4f}]:")
        print(f"{passage[:150]}...\n")

    return relevant_passages, relevance_scores
