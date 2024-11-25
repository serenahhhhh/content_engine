# Content Engine Chatbot

This project is a **Content Engine** that processes and interacts with textual data from PDFs, using embeddings and a query engine. It also includes a chatbot interface with a messaging app-style UI built in Streamlit.

---

## Project Structure


content_engine/
├── docs/                         # Folder for PDFs
│   ├── goog-10k-2023.pdf         # Example PDF document
│   ├── tsla-20231231-ge3n.pdf    # Example PDF document
│   └── uber-10-k-2023.pdf        # Example PDF document
├── pdf_processing.py             # PDF text extraction logic
├── embedding_generator.py        # Embedding generation logic
├── vector_store_manager.py       # Vector storage management
├── query_engine.py               # Query engine configuration
├── local_llm.py                  # Local LLM integration
├── chatbot_interface.py          # Streamlit-based chatbot interface
├── main.py                       # Main orchestrator script
├── requirements.txt              # Dependencies list
├── app.py                        # Streamlit app for chatbot interaction
└── README.md                     # Documentation and usage guide


---

## Features

1. **PDF Processing**:
   - Extracts text from PDF documents for analysis and embedding generation.

2. **Embedding Generation**:
   - Generates embeddings using OpenAI or other configured embedding models.

3. **Vector Store Management**:
   - Stores embeddings in a vector database for efficient similarity searches.

4. **Query Engine**:
   - Configures and executes queries on the vector database.

5. **Chatbot Interface**:
   - Provides a user-friendly chatbot in a messaging app style using `Streamlit`.

---

## Installation

1. Clone this repository:
   ```bash
   git clone <repository-url>
   cd content_engine


## Run the Streamlit Chatbot
streamlit run app.py

## Main Orchestrator
python main.py

