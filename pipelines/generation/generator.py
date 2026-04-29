import asyncio
from pipelines.generation.citations import parse_citations


async def mock_stream(query: str):
    # fake context (simulate retrieval)
    context_chunks = [
        {
            "chunk_id": "1",
            "document": "doc1.pdf",
            "page": 1,
            "text": "Artificial intelligence is simulation of human intelligence."
        }
    ]

    full_text = ""

    # STREAM START
    yield {"type": "retrieval_start"}

    await asyncio.sleep(0.5)

    yield {
        "type": "retrieval_complete",
        "chunk_count": len(context_chunks),
        "sources": [c["document"] for c in context_chunks]
    }

    await asyncio.sleep(0.5)

    # STREAM TOKENS
    tokens = [
        "Artificial ", "intelligence ", "is ",
        "the ", "simulation ", "of ",
        "human ", "intelligence ", "[Source ", "1]"
    ]

    last_keepalive = asyncio.get_event_loop().time()

    for t in tokens:
        full_text += t
        yield {"type": "token", "delta": t}

        await asyncio.sleep(0.2)

        # 🔥 KEEPALIVE every 15 sec
        now = asyncio.get_event_loop().time()
        if now - last_keepalive > 15:
            yield {"type": "keepalive"}
            last_keepalive = now

    # ✅ PARSE CITATIONS
    citations = parse_citations(full_text, context_chunks)

    # FINAL EVENT
    yield {
        "type": "done",
        "run_id": "abc-123",
        "citations": citations
    }