import fitz  # PyMuPDF
import json
import re
import os


def extract_text_from_pdf(pdf_path):
    print(f"Checking if file exists: {pdf_path}")
    if not os.path.exists(pdf_path):
        print(f"File not found: {pdf_path}")
        return ""
    if not os.access(pdf_path, os.R_OK):
        print(f"File not readable: {pdf_path}")
        return ""

    try:
        print(f"Opening PDF file: {pdf_path}")
        document = fitz.open(pdf_path)
        text = ""
        for page_num in range(len(document)):
            print(f"Reading page {page_num + 1}")
            page = document.load_page(page_num)
            text += page.get_text()
        print(f"Text extraction complete")
        return text
    except Exception as e:
        print(f"Error reading PDF: {e}")
        return ""


def extract_numbers_from_text(text):
    # Find all numbers in the text
    numbers = re.findall(r'\d+\.?\d*', text)
    return numbers


def main(pdf_path):
    # Extract text from PDF
    text = extract_text_from_pdf(pdf_path)

    if text:
        # Extract numbers from the text
        numbers = extract_numbers_from_text(text)

        # Save numbers to JSON file
        output_path = "/app/outputs/extracted_numbers.json"
        with open(output_path, "w") as f:
            json.dump(numbers, f)

        print(f"Numbers extracted and saved to {output_path}")
    else:
        print("No text extracted from PDF.")


if __name__ == "__main__":
    pdf_path = "/app/test.pdf"
    main(pdf_path)
