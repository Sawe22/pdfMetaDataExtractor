

from PyPDF2 import PdfReader

def extract_information(pdf_path):
    with open(pdf_path, 'rb') as f:
        pdf = PdfReader(f)
        information = pdf.metadata
        number_of_pages = len(pdf.pages)

    return {
        'Author': information.author,
        'Creator': information.creator,
        'Producer': information.producer,
        'Subject': information.subject,
        'Title': information.title,
        'Number of pages': number_of_pages
    }