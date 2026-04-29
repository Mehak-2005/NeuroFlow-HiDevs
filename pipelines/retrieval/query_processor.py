class QueryProcessor:
    async def process(self, query: str):
        return {
            "original": query,
            "expanded": [query],  # simple for now
            "filters": {},
            "type": "factual"
        }