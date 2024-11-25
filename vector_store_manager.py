from langchain.embeddings import OpenAIEmbeddings
import json
import os

openai_api_key = "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"  # Replace with your actual OpenAI API key

class VectorStoreManager:
    def __init__(self, vector_file, openai_api_key="YOUR_OPENAI_API_KEY"):
        self.vector_file = vector_file
        self.openai_api_key = openai_api_key
        self.vectors = self.load_vectors()
        self.embeddings = OpenAIEmbeddings(openai_api_key=openai_api_key)

    def load_vectors(self):
        if os.path.exists(self.vector_file):
            with open(self.vector_file, "r", encoding="utf-8") as f:
                return json.load(f)
        return []

    def save_vectors(self):
        with open(self.vector_file, "w", encoding="utf-8") as f:
            json.dump(self.vectors, f, ensure_ascii=False, indent=4)

    def create_embedding(self, text):
        return self.embeddings.embed_documents([text])[0]

    def add_vector(self, vector):
        self.vectors.append(vector)
        self.save_vectors()

    def get_vectors(self):
        return self.vectors
