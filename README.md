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
