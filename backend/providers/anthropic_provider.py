import anthropic
from .base import BaseLLMProvider, ChatMessage

client = anthropic.AsyncAnthropic()

class AnthropicProvider(BaseLLMProvider):

    async def complete(self, messages, **kwargs):
        res = await client.messages.create(
            model="claude-3-haiku-20240307",
            messages=[{"role": m.role, "content": m.content} for m in messages]
        )
        return res

    async def stream(self, messages, **kwargs):
        async with client.messages.stream(
            model="claude-3-haiku-20240307",
            messages=[{"role": m.role, "content": m.content} for m in messages]
        ) as stream:
            async for text in stream.text_stream:
                yield text

    async def embed(self, texts):
        return []  # simple placeholder

    @property
    def cost_per_input_token(self):
        return 0.0

    @property
    def cost_per_output_token(self):
        return 0.0

    @property
    def context_window(self):
        return 200000