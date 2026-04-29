import tiktoken

class ContextAssembler:
    def __init__(self):
        self.encoder = tiktoken.get_encoding("cl100k_base")

    def assemble(self, chunks, max_tokens=4000):
        context = ""
        total_tokens = 0

        for chunk in chunks:
            tokens = len(self.encoder.encode(chunk))
            if total_tokens + tokens > max_tokens:
                break

            context += f"\n{chunk}\n"
            total_tokens += tokens

        return {
            "context": context,
            "total_tokens": total_tokens
        }