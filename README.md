# Task 13 — Security Hardening

## Overview
This task focuses on securing the NeuroFlow backend against unauthorized access, prompt injection attacks, secret leakage, SSRF attacks, and unsafe file uploads.

The following security features were implemented:

- JWT Authentication & Authorization
- Scope-based Access Control
- Input Validation & Sanitization
- Prompt Injection Detection
- Secret Detection & Redaction
- SSRF Protection
- File MIME & Magic Byte Validation
- Security Headers Middleware
- detect-secrets Integration

---

# Features Implemented

## 1. JWT Authentication

Implemented JWT-based authentication using `python-jose`.

### Endpoint
`POST /auth/token`

### Request
```json
{
  "client_id": "admin_client",
  "client_secret": "admin_secret"
}
```
### Response
```
{
  "access_token": "jwt_token_here",
  "token_type": "bearer",
  "expires_in": 3600
}
```
### JWT Payload
```
{
  "sub": "client_id",
  "scopes": ["query", "ingest", "admin"],
  "exp": 1234567890
}
```
# Protected Routes

## All endpoints except:
```
/health
/metrics
```
require:
```
Authorization: Bearer <token>
```
### 2. Scope-Based Authorization

Implemented role/scope validation using FastAPI dependencies.

Scope Rules
Endpoint	Required Scope
```
/query	query
/ingest	ingest
/pipelines	admin
Fine-tuning endpoints	admin
```
Example

A token with only query scope cannot access:
```
POST /pipelines
```
Returns:
```
{
  "detail": "Insufficient permissions"
}
```
### 3. Input Validation & Sanitization

Implemented centralized validation inside:

backend/security/validators.py
Validations Added
HTML Sanitization

All text inputs are sanitized using:

bleach.clean(text, tags=[], strip=True)
Maximum Length Validation
Input	Max Length
Query Text	5000
Pipeline Name	100
URL Validation

Only valid HTTP/HTTPS URLs allowed.

Regex used:
```
^https?://
SSRF Protection
```
Blocked:
```
localhost
127.0.0.1
10.x.x.x
172.16.x.x
192.168.x.x
```
Example blocked request:
```
{
  "url": "http://192.168.1.1"
}
```
Returns:
```
{
  "error": "invalid_url"
}
```
File Validation

Implemented:

MIME type validation
Magic byte validation

Fake files (e.g. renamed executables as .pdf) are rejected.

### 4. Prompt Injection Detection

Implemented in:
```
backend/security/prompt_injection.py
```
#### Layer 1 — Pattern Matching

The following patterns are scanned:
```
INJECTION_PATTERNS = [
    r"ignore (all |previous |the |your )?instructions",
    r"you are now",
    r"new (system |)prompt",
    r"disregard (the |all |previous )",
    r"forget (everything|all|previous)",
    r"act as (if |a |an )",
    r"\[\[(system|SYSTEM)\]\]",
    r"<\|system\|>"
]
```
Behavior

If detected:

Logs warning
Adds metadata:
{
  "prompt_injection_detected": true,
  "pattern": "matched_pattern"
}

Documents are NOT rejected.

#### Layer 2 — LLM-Based Detection

For user queries:

Query is classified for prompt injection attempts.
If malicious:

Returns:
```
{
  "error": "query_rejected",
  "reason": "potential_prompt_injection"
}
```
HTTP Status:
```
400 Bad Request
```
### 5. Secret Detection & Redaction

Implemented in:

backend/security/secret_detector.py
Detected Secrets
AWS Keys
AKIA[0-9A-Z]{16}
Generic API Keys
['"]?(?:api|secret|token|key|password)['"]?\s*[:=]\s*['"][A-Za-z0-9/+]{20,}['"]
JWT Tokens

Detected using:

xxx.yyy.zzz
PEM Private Keys

Detects:

-----BEGIN PRIVATE KEY-----
Redaction

Secrets are replaced with:

[REDACTED]
Example

Before:

AWS_KEY=AKIA1234567890ABCDE

After:

AWS_KEY=[REDACTED]
Logging

Logs event:
```
{
  "event": "secret_redacted",
  "document_id": "doc_123",
  "pattern_type": "aws_key"
}
```
Raw secrets are never stored in the vector database.

### 6. Security Headers Middleware

Added middleware to attach secure HTTP headers.
```
Headers Added
{
    "X-Content-Type-Options": "nosniff",
    "X-Frame-Options": "DENY",
    "Strict-Transport-Security": "max-age=31536000",
    "Content-Security-Policy": "default-src 'self'",
    "X-Request-ID": str(uuid.uuid4())
}
```
### 7. detect-secrets Integration

Installed:
```
pip install detect-secrets
```
Generated baseline:
```
detect-secrets scan --baseline .secrets.baseline
```
Committed:
```
.secrets.baseline
```
Validation:
```
detect-secrets scan --baseline .secrets.baseline
```
Exits successfully with:

exit code 0

# Project Structure
```
backend/
│
├── security/
│   ├── __init__.py
│   ├── prompt_injection.py
│   ├── secret_detector.py
│   └── validators.py
│
├── requirements.txt
│
└── ...
Installation
Create Branch
git checkout task-42
git checkout -b task-43
Activate Environment
cd backend
source venv/bin/activate
Install Dependencies
pip install python-jose[cryptography] bleach detect-secrets
Update Requirements
pip freeze > requirements.txt
Running Security Tests
```
# Test Authentication

Without token:
```
GET /query
```
Expected:
```
401 Unauthorized
Test Scope Validation
```
Use query-scoped token on admin endpoint:
```
POST /pipelines
```
Expected:
```
403 Forbidden
Test SSRF Protection
{
  "url": "http://192.168.1.1"
}
```
Expected:
```
400 Bad Request
Test Prompt Injection
```
Input:
```
Ignore all previous instructions
```
Expected:

Pattern detection triggered
Query rejected by LLM layer
Test Secret Redaction

Input document containing:
```
AKIA1234567890ABCDE
```
Expected stored chunk:
```
[REDACTED]
Git Commands
Commit Changes
git add backend/security/ .secrets.baseline backend/requirements.txt
git commit -m "feat: security hardening with JWT auth, input validation, and prompt injection defense"
Push Branch
git push -u origin task-43
```
# Final Verification Checklist
 JWT authentication implemented
 Protected routes secured
 Scope-based authorization added
 HTML sanitization enabled
 File MIME + magic byte validation implemented
 SSRF protection added
 Prompt injection detection implemented
 Secret redaction implemented
 Security middleware added
 detect-secrets baseline committed
 Security tests completed successfully
 
 #  Outcome

The NeuroFlow backend is now hardened against:

Unauthorized access
Prompt injection attacks
Secret leakage
SSRF exploitation
Unsafe file uploads
Header-based attacks

This implementation significantly improves the overall security posture of the RAG pipeline.
