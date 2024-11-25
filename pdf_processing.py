import pdfplumber
import os

def extract_text_from_pdf(pdf_path):
    """Extract text from a PDF file."""
    with pdfplumber.open(pdf_path) as pdf:
        text = ""
        for page in pdf.pages:
            text += page.extract_text()
    return text

def process_pdfs():
    """Process and save extracted text from PDF files."""
    # Define paths to PDFs
    pdf_paths = [
        r"C:\Users\Lenovo\OneDrive\Desktop\vs\content_engine\docs\goog-10-k-2023(1).pdf",
        r"C:\Users\Lenovo\OneDrive\Desktop\vs\content_engine\docs\tsla-20231231-gen.pdf",
        r"C:\Users\Lenovo\OneDrive\Desktop\vs\content_engine\docs\uber-10-k-2023.pdf"
    ]

    # Ensure the docs folder exists
    docs_folder = r"C:\Users\Lenovo\OneDrive\Desktop\vs\content_engine\docs"
    if not os.path.exists(docs_folder):
        os.makedirs(docs_folder)

    # Parse all PDFs and save as text files
    for idx, pdf_path in enumerate(pdf_paths, 1):
        text = extract_text_from_pdf(pdf_path)
        with open(f"{docs_folder}\\pdf{idx}_text.txt", "w", encoding="utf-8") as f:
            f.write(text)
    print("Text extraction and saving completed.")

if __name__ == "__main__":
    process_pdfs()
