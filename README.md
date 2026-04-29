# Task 5 — Retrieval Pipeline (Hybrid Search)

## 📌 Overview

Implemented hybrid retrieval with ranking and scoring.

## ✅ Components

* Query Processor
* Retriever (similarity search)
* Fusion (RRF)
* Reranker
* Context Assembler

## 🧪 Test

```bash
python test_retrieval.py
```

## ✅ Output

```bash
RESULTS: [
  {"text": "...", "score": 0.8},
  {"text": "...", "score": 0.7}
]
```

## 🧠 Features

* Async retrieval
* Ranked results
* Structured output

## 🧠 Tech

* NumPy
* Sentence Transformers (optional)
