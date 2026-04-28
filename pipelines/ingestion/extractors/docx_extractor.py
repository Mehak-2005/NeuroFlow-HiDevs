from docx import Document
from . import ExtractedPage

def extract_docx(file_path):
    doc = Document(file_path)
    pages = []

    for i, para in enumerate(doc.paragraphs):
        pages.append(ExtractedPage(
            page_number=i,
            content=para.text,
            content_type="text",
            metadata={}
        ))

    return pages