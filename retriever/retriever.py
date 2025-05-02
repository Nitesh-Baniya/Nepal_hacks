import numpy as np
from sklearn.metrics.pairwise import cosine_similarity


def retrieve_relevant_context(query_embedding, policies, embeddings, top_k=1):
    sims = cosine_similarity([query_embedding], embeddings)[0]
    top_idx = np.argsort(sims)[-top_k:][::-1]
    relevant_policies = [policies[i] for i in top_idx]
    return relevant_policies, sims[top_idx]
