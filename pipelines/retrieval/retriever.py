import asyncio

class Retriever:
    async def retrieve(self, query: str, k: int = 10):
        results = await asyncio.gather(
            self._dense(query, k),
            self._sparse(query, k),
            self._metadata(query, k)
        )
        return results

    async def _dense(self, query, k):
        return []

    async def _sparse(self, query, k):
        return []

    async def _metadata(self, query, k):
        return []