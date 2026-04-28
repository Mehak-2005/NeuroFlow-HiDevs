import httpx
import trafilatura
from . import ExtractedPage

async def extract_url(url):
    async with httpx.AsyncClient() as client:
        res = await client.get(url)

    content = trafilatura.extract(res.text)

    return [ExtractedPage(
        page_number=0,
        content=content or "",
        content_type="text",
        metadata={"url": url}
    )]