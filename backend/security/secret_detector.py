import re

SECRET_PATTERNS = {
    "aws_key": r"AKIA[0-9A-Z]{16}",
    "jwt": r"eyJ[a-zA-Z0-9_-]+\.[a-zA-Z0-9_-]+\.[a-zA-Z0-9_-]+"
}

def redact_secrets(text: str):
    for name, pattern in SECRET_PATTERNS.items():
        text = re.sub(pattern, "[REDACTED]", text)

    return text