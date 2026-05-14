import asyncio

from providers.base import ChatMessage
from providers.client import NeuroFlowClient


async def test():
    client = NeuroFlowClient()

    print("Embedding:")
    emb = await client.embed(["hello world"])
    print(emb[0][:5])

    print("\nStreaming:")
    messages = [ChatMessage(role="user", content="Say one word")]

    provider = client.providers["openai"]

    async for token in provider.stream(messages):
        print(token, end="", flush=True)


asyncio.run(test())
