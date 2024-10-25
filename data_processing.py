import os
from PyPDF2 import PdfReader

def extract_text_from_pdf(file_path):
    """Extract text from a given PDF file."""
    reader = PdfReader(file_path)
    text = ""
    for page in reader.pages:
        text += page.extract_text()
    return text

def save_processed_data(text, save_path):
    """Save processed text data to a specified path."""
    with open(save_path, "w") as f:
        f.write(text)
    print(f"Processed data saved to {save_path}")

def process_raw_data():
    """Process all raw data in the specified directory."""
    raw_data_path = "data/raw/"
    processed_data_path = "data/processed/"

    for filename in os.listdir(raw_data_path):
        if filename.endswith(".pdf"):
            file_path = os.path.join(raw_data_path, filename)
            text = extract_text_from_pdf(file_path)
            processed_file_path = os.path.join(processed_data_path, f"processed_{filename[:-4]}.txt")
            save_processed_data(text, processed_file_path)

if __name__ == "__main__":
    process_raw_data()