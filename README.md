# Task 4 — Multi-Modal Ingestion Pipeline

## 📌 Overview

Built async ingestion pipeline for multiple data formats.

## ✅ Supported

* PDF
* DOCX
* Images (OCR)
* CSV
* URLs

## ✅ Features

* Modular extractors
* Chunking
* Deduplication
* Async processing

## 🚀 Run

```bash
uvicorn main:app --reload
```

## 🧪 Test

```bash
curl -F "file=@sample.pdf" http://localhost:8000/ingest
```

## ✅ Output

```json
{
  "message": "File processed successfully"
}
```

## 🧠 Tech

* pdfplumber
* pytesseract
* pandas
* trafilatura
