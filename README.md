# Task 16 — CI/CD Pipeline

## Overview

This task implements a production-grade CI/CD pipeline for NeuroFlow using GitHub Actions.

The pipeline automates:
- linting
- type checking
- unit testing
- security scanning
- Docker image building
- quality gate validation

---

# Features Implemented

## GitHub Actions Workflows

Implemented workflows inside:

```bash
.github/workflows/
```

### Workflows

| Workflow | Purpose |
|---|---|
| ci.yml | Linting, testing, security scanning |
| build.yml | Docker image build pipeline |
| quality-gate.yml | Nightly quality checks |

---

# CI Workflow

File:

```bash
.github/workflows/ci.yml
```

### Jobs

## Lint Job

Runs:
- Ruff
- MyPy

Commands:

```bash
ruff check backend/
mypy backend/ --ignore-missing-imports
```

---

## Test Job

Runs:
- Pytest
- Coverage reporting

Services:
- PostgreSQL
- Redis

Command:

```bash
pytest tests/unit/ -v --cov=backend --cov-report=xml
```

---

## Security Job

Runs:
- detect-secrets
- pip-audit

Purpose:
- dependency vulnerability scanning
- secret detection

---

# Build Workflow

File:

```bash
.github/workflows/build.yml
```

Features:
- Docker Buildx
- GHCR authentication
- Docker image builds
- image validation

---

# Quality Gate Workflow

File:

```bash
.github/workflows/quality-gate.yml
```

Runs nightly at:
```text
2 AM
```

Checks:
- Retrieval benchmark quality
- MRR threshold validation

Fails pipeline if:
```text
MRR < 0.55
```

---

# Ruff Configuration

Defined in:

```bash
pyproject.toml
```

Features:
- Python 3.11 support
- strict linting
- async checks
- naming validation

---

# MyPy Configuration

Strict type checking enabled.

```toml
strict = true
```

---

# Unit Tests

Implemented inside:

```bash
tests/unit/
```

### Test Files

| File | Purpose |
|---|---|
| test_chunker.py | Chunking validation |
| test_fusion.py | RRF logic tests |
| test_circuit_breaker.py | State transitions |
| test_prompt_injection.py | Injection detection |
| test_pipeline_config.py | Config validation |

Minimum:
```text
5 tests per file
```

---

# Running Locally

## Run Ruff

```bash
ruff check backend/
```

---

## Run MyPy

```bash
mypy backend/ --ignore-missing-imports
```

---

## Run Unit Tests

```bash
pytest tests/unit/ -v
```

---

# GitHub Actions Verification

Open:
```text
GitHub Repository → Actions Tab
```

Verify:
- CI passes
- Build passes
- Security checks pass

---

# Final Outcome

NeuroFlow now includes:
- automated CI/CD
- linting and type validation
- automated security scanning
- Docker build automation
- nightly quality gates
- reliable unit testing pipeline

This ensures every push is validated automatically before deployment.
