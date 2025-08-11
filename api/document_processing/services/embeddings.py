from sentence_transformers import SentenceTransformer


model = SentenceTransformer("sentence-transformers/all-MiniLM-L12-v2")


class EmbeddingsService:

    @staticmethod
    def generate_embedding(doc_content: str):
        return model.encode(doc_content).tolist()
