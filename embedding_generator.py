    
import os
import json
from langchain.embeddings import OpenAIEmbeddings

openai_api_key = "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"  # Replace with your actual OpenAI API key


def generate_embeddings(text_files):
    """Generate and save embeddings for the text files."""
    embeddings = OpenAIEmbeddings(openai_api_key=openai_api_key)  # Initialize the embeddings
    vectors = []
    
    for text_file in text_files:
        with open(text_file, "r", encoding="utf-8") as f:
            text = f.read()
        
        # Generate embeddings for each document's text
        vector = embeddings.embed_documents([text])
        vectors.append(vector)
    
    # Save the embeddings to a JSON file
    embeddings_file = r"C:\Users\Lenovo\OneDrive\Desktop\vs\content_engine\docs\embeddings.json"
    with open(embeddings_file, "w", encoding="utf-8") as f:
        json.dump(vectors, f, ensure_ascii=False, indent=4)
    
    print(f"Embeddings saved to {embeddings_file}")

if __name__ == "__main__":
    text_files = [
        r"C:\Users\Lenovo\OneDrive\Desktop\vs\content_engine\docs\pdf1_text.txt",
        r"C:\Users\Lenovo\OneDrive\Desktop\vs\content_engine\docs\pdf2_text.txt",
        r"C:\Users\Lenovo\OneDrive\Desktop\vs\content_engine\docs\pdf3_text.txt"
    ]
    generate_embeddings(text_files)
