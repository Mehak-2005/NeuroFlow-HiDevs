from .openai_provider import OpenAIProvider
from .anthropic_provider import AnthropicProvider
from .router import ModelRouter

class NeuroFlowClient:

    def __init__(self):
        self.router = ModelRouter()
        self.providers = {
            "openai": OpenAIProvider(),
            "anthropic": AnthropicProvider()
        }

    async def chat(self, messages, criteria):
        provider_key = self.router.route(criteria)
        provider = self.providers[provider_key]
        return await provider.complete(messages)

    async def embed(self, texts):
        return await self.providers["openai"].embed(texts)