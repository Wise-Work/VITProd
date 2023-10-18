# Extract information form a PDF file and return a list of strings

from PyPDF2 import PdfFileReader

def extract_pdf_info(pdf_file):
    pdf = PdfFileReader(pdf_file)
    number_of_pages = pdf.getNumPages()

    text = ""
    for i in range(number_of_pages):
        text += pdf.getPage(i).extractText() + "\n"

    return text

