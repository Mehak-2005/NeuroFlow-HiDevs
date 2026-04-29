def build_prompt(query: str, context_chunks: list[str], query_type="factual"):
    context_text = "\n\n".join(
        [f"[Source {i+1}] {chunk}" for i, chunk in enumerate(context_chunks)]
    )

    base = """You are a precise research assistant. Answer the user's question using ONLY the provided context.
If the context does not contain enough information, say so.
Cite sources like [Source N]."""

    rules = {
        "factual": "Provide a concise answer.",
        "analytical": "Analyze across sources.",
        "comparative": "Compare in structured format.",
        "procedural": "Provide numbered steps."
    }

    return f"""{base}

{rules.get(query_type)}

<context>
{context_text}
</context>

Question: {query}
"""