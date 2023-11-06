import fitz  # PyMuPDF

def extract_text_from_pdf(pdf_path):
    pdf_document = fitz.open(pdf_path)
    text = ''
    for page_num in range(pdf_document.page_count):
        page = pdf_document.load_page(page_num)
        text += page.get_text()
    pdf_document.close()
    return text

def segment_document(document_text):
    sections = {
        "Abstract": "",
        "Introduction": "",
        "Methodology": "",
        "Results": "",
        "Conclusion": ""
    }

    current_section = None
    for line in document_text.split('\n'):
        for section in sections:
            if section.lower() in line.lower():
                current_section = section
                break
        if current_section:
            sections[current_section] += line + '\n'

    return sections

def process_pdf_and_segment(pdf_path):
    pdf_text = extract_text_from_pdf(pdf_path)
    segmented_sections = segment_document(pdf_text)
    return segmented_sections

def write_segmented_text_to_file(segmented_sections, output_file):
    with open(output_file, 'w', encoding='utf-8') as file:
        for section, text in segmented_sections.items():
            file.write(f"--- {section.capitalize()} ---\n")
            file.write(text)
            file.write("----------\n")

# Example usage
pdf_file_path = "path/to/your/file.pdf"
output_file_path = "path/to/segmented_output.txt"

sections = process_pdf_and_segment(pdf_file_path)
write_segmented_text_to_file(sections, output_file_path)