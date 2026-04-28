import pypdfium2 as pdfium
from . import ExtractedPage

def extract_pdf(file_path):
    pdf = pdfium.PdfDocument(file_path)
    pages = []

    for i in range(len(pdf)):
        text = pdf[i].get_textpage().get_text_range()

        pages.append(ExtractedPage(
            page_number=i,
            content=text,
            content_type="text",
            metadata={}
        ))

    return pages