from embedder.embedder import create_embeddings, embed_query
from retriever.retriever import retrieve_relevant_context
from generator.generator import generate_answer


def run_rag_pipeline(query, policies):
    embeddings = create_embeddings(policies)
    query_emb = embed_query(query)
    context, scores = retrieve_relevant_context(query_emb, policies, embeddings)
    if scores[0] > 0.6:
        return generate_answer(query, context)
    else:
        return f"**Requirement**:\n\n {query} \n\n **Status**: Missing \n\n**Reason**: \n\nThe requirement is missing."
