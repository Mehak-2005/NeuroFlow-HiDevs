# Task 17 – Backend Deployment on Railway

## Overview

This task focused on deploying the NeuroFlow backend to Railway using Docker, configuring the required infrastructure services, and validating application startup.

---

## Deployment Details

### Platform
- Railway

### Branch
- task-17

### Root Directory
- backend

### Deployment Method
- Dockerfile-based deployment

---

## Infrastructure Setup

### PostgreSQL
- Railway PostgreSQL service configured
- Database URL connected through environment variables

### Redis
- Railway Redis service configured
- Redis URL connected through environment variables

---

## Environment Variables

Configured variables include:

```env
POSTGRES_URL=<Railway Postgres Reference>
DATABASE_URL=<Railway Postgres Reference>
REDIS_URL=<Railway Redis Reference>
MLFLOW_URL=http://localhost:5000
```

Additional application-specific variables were configured as required.

---

## Docker Configuration

Deployment uses:

```dockerfile
backend/Dockerfile
```

Dependencies are installed through:

```text
requirements-docker.txt
```

Key fixes included:

- Added asyncpg
- Added redis
- Added prometheus-client
- Added python-multipart
- Added sse-starlette
- Added pydantic-settings
- Added python-jose

---

## Issues Encountered

### Dependency Errors

Resolved:

```text
ModuleNotFoundError: asyncpg
ModuleNotFoundError: redis
ModuleNotFoundError: prometheus_client
ModuleNotFoundError: python_multipart
ModuleNotFoundError: sse_starlette
ModuleNotFoundError: pydantic_settings
ModuleNotFoundError: jose
```

### Import Path Issues

Resolved incorrect imports:

```python
from backend.api...
```

Updated to:

```python
from api...
```

### Missing Modules

Some modules referenced non-existent packages:

```python
pipelines.*
```

Affected routers were temporarily disabled to allow application startup.

### Configuration Issues

Resolved:

```text
POSTGRES_URL missing
MLFLOW_URL missing
Invalid PostgreSQL DSN
```

---

## Verification

### Deployment Status

```text
ACTIVE
```

### Application Server

```text
Uvicorn running on port 8000
Application startup complete
```

### Public Domain

```text
https://neuroflow-hidevs-production.up.railway.app
```

---

## Deliverables

- Railway deployment configured
- Docker deployment operational
- PostgreSQL integrated
- Redis integrated
- Environment variables configured
- Backend service successfully deployed
- Health endpoint configured

---

## Repository

Branch:

```text
task-17
```

Repository:

```text
Mehak-2005/NeuroFlow-HiDevs
```

---

## Author

Mehak
