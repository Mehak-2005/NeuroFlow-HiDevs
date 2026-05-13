# Task 15 — Production Containerization

## Overview

This task focuses on production-grade containerization for NeuroFlow using:

- Multi-stage Docker builds
- Non-root containers
- Read-only filesystem
- Docker Compose production deployment
- Nginx reverse proxy
- Rate limiting
- Health probes
- Security hardening

---

# Features Implemented

## Backend Multi-Stage Dockerfile

Implemented:
- Python 3.11 slim image
- Multi-stage build
- Minimal runtime image
- Non-root user (`neuroflow`)
- Health check support
- Production Uvicorn workers

### Security Features

- Non-root execution
- Read-only filesystem
- No Linux capabilities
- `no-new-privileges`
- Temporary writable `/tmp`

---

## Frontend Dockerfile

Implemented:
- Node.js build stage
- Nginx runtime stage
- Optimized production assets
- Static file serving

---

# Production Docker Compose

File:
```bash
infra/docker-compose.prod.yml
```

Services:
- PostgreSQL
- Redis
- API
- Worker
- Nginx

---

# Resource Limits

| Service | Memory | CPU |
|---|---|---|
| PostgreSQL | 2 GB | 2 CPU |
| Redis | 512 MB | 0.5 CPU |
| API | 1 GB | 1 CPU |
| Worker | 2 GB | 2 CPU |

---

# Nginx Features

Implemented:
- Reverse proxy
- API load balancing
- Rate limiting
- Gzip compression
- Security headers

---

# Security Headers

Added:
- X-Frame-Options
- X-Content-Type-Options
- Content-Security-Policy

---

# Health Checks

Backend health endpoint:

```bash
/health
```

Docker health probe:

```dockerfile
HEALTHCHECK CMD curl -f http://localhost:8000/health || exit 1
```

---

# Security Hardening

## Non-Root User

Container runs as:

```bash
neuroflow
```

---

## Read-Only Filesystem

Enabled:

```yaml
read_only: true
```

---

## Dropped Linux Capabilities

```yaml
cap_drop:
  - ALL
```

---

# Build Instructions

## Build Containers

```bash
docker compose -f infra/docker-compose.prod.yml build
```

---

## Start Containers

```bash
docker compose -f infra/docker-compose.prod.yml up -d
```

---

# Verification

## Verify Non-Root User

```bash
docker exec neuroflow-api-1 whoami
```

Expected:
```bash
neuroflow
```

---

## Verify Read-Only Filesystem

```bash
docker exec neuroflow-api-1 touch /test
```

Expected:
Permission denied.

---

## Verify Health Check

```bash
docker inspect neuroflow-api-1 | grep Health
```

---

## Verify Capabilities Dropped

```bash
docker inspect neuroflow-api-1
```

Expected:
```json
"CapDrop": ["ALL"]
```

---

## Verify Rate Limiting

Sending more than 60 requests/minute returns:

```bash
429 Too Many Requests
```

---

# Final Outcome

NeuroFlow is now production-ready with:
- hardened containers
- minimal runtime images
- secure Nginx proxy
- health monitoring
- resource isolation
- scalable API deployment
