import re
from dataclasses import dataclass
from typing import List

@dataclass
class Citation:
    reference: str
    chunk_id: str
    document_name: str
    page_number: int | None
    content_preview: str


def parse_citations(text: str, context_chunks: list):
    pattern = r"\[Source (\d+)\]"
    matches = re.findall(pattern, text)

    citations = []

    for m in matches:
        idx = int(m) - 1

        if idx < len(context_chunks):
            chunk = context_chunks[idx]

            citations.append({
                "source": f"Source {m}",
                "chunk_id": chunk.get("chunk_id", "unknown"),
                "document": chunk.get("document", "unknown"),
                "page": chunk.get("page", None),
                "preview": chunk.get("text", "")[:100]
            })
        else:
            citations.append({
                "source": f"Source {m}",
                "invalid_citation": True
            })

    return citations