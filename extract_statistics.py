import fitz  # PyMuPDF
import json
import re
import os
from transformers import AutoTokenizer, AutoModelForTokenClassification
import torch

def extract_text_from_pdf(pdf_path):
    try:
        document = fitz.open(pdf_path)
        text = ""
        for page_num in range(len(document)):
            page = document.load_page(page_num)
            text += page.get_text()
        return text
    except Exception as e:
        print(f"Error reading PDF: {e}")
        return ""

def identify_statistical_sentences(text, model, tokenizer):
    sentences = text.split('. ')
    statistical_sentences = []

    for sentence in sentences:
        inputs = tokenizer(sentence, return_tensors="pt")
        outputs = model(**inputs)
        predictions = torch.argmax(outputs.logits, dim=-1)
        if predictions[0][1] == 1:  # Assuming the model marks statistical sentences with 1
            statistical_sentences.append(sentence)

    return statistical_sentences

def extract_title(text):
    title_pattern = r'^(.*?)\n'
    match = re.search(title_pattern, text.strip())
    return match.group(1) if match else ""

def extract_publication_year(text):
    year_pattern = r'\b(19|20)\d{2}\b'
    match = re.search(year_pattern, text)
    return match.group() if match else ""

def extract_abstract(text):
    abstract_pattern = r'(?i)abstract\s*(.*?)(?:\n\n|\Z)'
    match = re.search(abstract_pattern, text, re.DOTALL)
    return match.group(1).strip() if match else ""

def extract_numbers_and_statistics(text):
    # Refine patterns to exclude irrelevant numbers
    number_pattern = r'\b\d+(\.\d+)?\b'
    statistical_terms = ['mean', 'median', 'mode', 'standard deviation', 'variance', 'correlation', 'p-value',
                         'f-test', 'z-test', 'anova', 'chi-squared']
    statistics = {}

    for term in statistical_terms:
        pattern = rf'([^.]*\b{term}\b[^.]*)'
        matches = re.findall(pattern, text, flags=re.IGNORECASE)
        for match in matches:
            statistics[match] = re.findall(number_pattern, match)

    return statistics

def extract_section(text, section_title):
    pattern = rf'{section_title}[:\n\s]*\n+(.*?)(?=\n{2,}[A-Z]|\Z)'
    match = re.search(pattern, text, re.IGNORECASE | re.DOTALL)
    if match:
        return match.group(1).strip()
    return ""

def extract_all_sections(text):
    sections = {
        "Source citation": extract_section(text, "citation"),
        "Publication name": extract_section(text, "publication name"),
        # "Publication year": extract_section(text, "publication year"),
        "Publication year": extract_publication_year(text),
        "Publication type": extract_section(text, "publication type"),
        "Title": extract_title(text),
        # "Article abstract": extract_section(text, "abstract"),
        "Article abstract": extract_abstract(text),
        "Hypotheses": extract_section(text, "hypotheses"),
        "Sample size": extract_section(text, "sample size"),
        "Participant mean age": extract_section(text, "participant mean age"),
        "Participants' age Standard Deviation": extract_section(text, "age standard deviation"),
        "Number of Females": extract_section(text, "number of females"),
        "Participants' Country of Origin": extract_section(text, "country of origin"),
        "Sample Type": extract_section(text, "sample type"),
        "Participant education Level": extract_section(text, "education level"),
        "Participant Race or Ethnicity": extract_section(text, "race or ethnicity"),
        "Research Method": extract_section(text, "research method"),
        "Study Setting": extract_section(text, "study setting"),
        "Research task description for participants": extract_section(text, "task description"),
        "Task Duration": extract_section(text, "task duration"),
        "Other statistics": extract_numbers_and_statistics(text)  # Use the existing function here
    }
    return sections

def main(pdf_path):
    # Load SciBERT model and tokenizer
    tokenizer = AutoTokenizer.from_pretrained("allenai/scibert_scivocab_uncased")
    model = AutoModelForTokenClassification.from_pretrained("allenai/scibert_scivocab_uncased")

    # Extract text from PDF
    text = extract_text_from_pdf(pdf_path)

    if text:
        # Extract targeted statistics
        statistics = extract_all_sections(text)

        # Debugging: Print extracted text for each section
        for section, content in statistics.items():
            print(f"Extracted for {section}: {content}")

        # Save statistics to JSON file
        output_path = "/app/outputs/statistics.json"
        with open(output_path, "w") as f:
            json.dump(statistics, f, indent=4)

        print(f"Statistics extracted and saved to {output_path}")
    else:
        print("No text extracted from PDF.")

if __name__ == "__main__":
    pdf_path = "/app/test3.pdf"
    main(pdf_path)