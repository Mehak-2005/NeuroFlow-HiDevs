import re

import bleach
from fastapi import HTTPException

MAX_QUERY_LENGTH = 5000


def sanitize_text(text: str):
    return bleach.clean(text, tags=[], strip=True)


def validate_query(text: str):
    if len(text) > MAX_QUERY_LENGTH:
        raise HTTPException(status_code=400, detail="Query too long")

    return sanitize_text(text)


def validate_url(url: str):
    if not re.match(r"^https?://", url):
        raise HTTPException(status_code=400, detail="Invalid URL")

    blocked = ["127.0.0.1", "localhost", "192.168.", "10.", "172.16."]

    for item in blocked:
        if item in url:
            raise HTTPException(status_code=400, detail="Blocked private URL")

    return url
