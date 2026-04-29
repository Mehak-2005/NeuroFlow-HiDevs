# Task 2 — Infrastructure Foundation

## 📌 Overview

Set up production infrastructure using Docker.

## ✅ Services

* PostgreSQL (pgvector)
* Redis
* MLflow
* Jaeger

## 🚀 Start

```bash
cd infra
docker compose up -d
```

## 🔍 Check

```bash
docker ps
```

## 🔍 Health API

```
http://127.0.0.1:8000/health
```

## ✅ Output

```json
{
  "status": "ok",
  "checks": {
    "postgres": true,
    "redis": true,
    "mlflow": true
  }
}
```

## 🧠 Tech

* Docker
* PostgreSQL
* Redis
* MLflow
