from sentence_transformers import SentenceTransformer

model = SentenceTransformer("all-MiniLM-L6-v2")


def create_embeddings(policies):
    return model.encode(policies)


def embed_query(query):
    return model.encode([query])[0]
