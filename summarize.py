from transformers import pipeline
from PyPDF2 import PdfReader
import os

def extract_text_from_pdf(file_path):
    reader = PdfReader(file_path)
    text = ""
    for page in reader.pages:
        text += page.extract_text()
    return text

def summarize_text(text):
    summarizer = pipeline("summarization", model="facebook/bart-large-cnn")
    summary = summarizer(text, max_length=150, min_length=40, do_sample=False)
    return summary[0]["summary_text"]

def process_and_summarize(file_path, save_path):
    text = extract_text_from_pdf(file_path)
    summary = summarize_text(text)
    with open(save_path, "w") as f:
        f.write(summary)
    print(f"Summary saved to {save_path}")

if __name__ == "__main__":
    raw_path = os.path.join("data", "raw", "sample_study_material.pdf")
    summary_path = os.path.join("data", "processed", "summary.txt")
    process_and_summarize(raw_path, summary_path)