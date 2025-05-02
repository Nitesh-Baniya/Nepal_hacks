def cybersecurity_rag_system(query, df, embeddings, top_k=3):
    """
    Complete RAG system that retrieves context and generates an answer

    Args:
        query: User's question
        df: Knowledge base DataFrame
        embeddings: Pre-computed embeddings
        top_k: Number of passages to retrieve

    Returns:
        Generated answer
    """
    print(f"\nQuestion: {query}")

    # Retrieve relevant context
    relevant_passages, relevance_scores = retrieve_relevant_context(query, df, embeddings, top_k)

    # Generate answer
    answer = generate_answer(query, relevant_passages, relevance_scores)

    print("\n=== Generated Answer ===")
    display(Markdown(answer))

    return answer
