from query_engine import QueryEngine
from local_llm import LocalLLM
from vector_store_manager import VectorStoreManager
from langchain.embeddings import OpenAIEmbeddings

class ChatbotInterface:
    def __init__(self):
        self.vector_store_manager = VectorStoreManager("embeddings.json")
        self.embeddings_model = OpenAIEmbeddings(openai_api_key="YOUR_OPENAI_API_KEY")
        self.query_engine = QueryEngine(self.vector_store_manager, self.embeddings_model)
        self.local_llm = LocalLLM()

    def chat(self, user_input):
        query_result = self.query_engine.query(user_input)
        if query_result:
            return query_result
        else:
            return self.local_llm.generate_response(user_input)
