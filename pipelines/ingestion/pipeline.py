import hashlib
from .extractors.pdf_extractor import extract_pdf

def compute_hash(file_bytes):
    return hashlib.sha256(file_bytes).hexdigest()

def run_pipeline(file_path):
    pages = extract_pdf(file_path)

    all_chunks = []
    for page in pages:
        chunks = [page.content[i:i+500] for i in range(0, len(page.content), 500)]
        all_chunks.extend(chunks)

    return all_chunks