import time
import asyncio
from openai import AsyncOpenAI
from .base import BaseLLMProvider, ChatMessage, GenerationResult

client = AsyncOpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key="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"
)

PRICES = {
    "gpt-4o": {"input": 2.50 / 1e6, "output": 10.00 / 1e6},
    "gpt-4o-mini": {"input": 0.15 / 1e6, "output": 0.60 / 1e6}
}

class OpenAIProvider(BaseLLMProvider):

    def __init__(self, model="gpt-4o-mini"):
        self.model = model

    async def complete(self, messages, **kwargs):
        start = time.time()

        response = await client.chat.completions.create(
            model=self.model,
            messages=[{"role": m.role, "content": m.content} for m in messages]
        )

        latency = (time.time() - start) * 1000

        usage = response.usage

        cost = (
            usage.prompt_tokens * PRICES[self.model]["input"] +
            usage.completion_tokens * PRICES[self.model]["output"]
        )

        return GenerationResult(
            content=response.choices[0].message.content,
            model=self.model,
            input_tokens=usage.prompt_tokens,
            output_tokens=usage.completion_tokens,
            latency_ms=latency,
            cost_usd=cost,
            finish_reason=response.choices[0].finish_reason
        )

    async def stream(self, messages, **kwargs):
        stream = await client.chat.completions.create(
            model=self.model,
            messages=[{"role": m.role, "content": m.content} for m in messages],
            stream=True
        )

        async for chunk in stream:
            if chunk.choices[0].delta.content:
                yield chunk.choices[0].delta.content

    async def embed(self, texts):
        res = await client.embeddings.create(
            model="text-embedding-3-small",
            input=texts
        )
        return [d.embedding for d in res.data]

    @property
    def cost_per_input_token(self):
        return PRICES[self.model]["input"]

    @property
    def cost_per_output_token(self):
        return PRICES[self.model]["output"]

    @property
    def context_window(self):
        return 128000