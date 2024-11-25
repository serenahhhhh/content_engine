from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

class QueryEngine:
    def __init__(self, vector_store_manager, embeddings_model):
        self.vector_store_manager = vector_store_manager
        self.embeddings_model = embeddings_model

    def query(self, query_text):
        vectors = self.vector_store_manager.get_vectors()
        if not vectors:
            return "No data available in the vector store."

        query_vector = self.embeddings_model.embed_documents([query_text])[0]
        similarities = cosine_similarity([query_vector], vectors)
        best_match_idx = np.argmax(similarities)

        if similarities[0][best_match_idx] > 0.7:
            return f"Best match found: {vectors[best_match_idx]}"
        else:
            return "No relevant results found in the vector store."
