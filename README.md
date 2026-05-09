# NeuroFlow — Task 11
Next.js Dashboard — Pipeline Visualization, Query Playground & Live Evaluation Feed

This task implements the complete frontend dashboard for NeuroFlow using Next.js 14, TypeScript, Tailwind CSS, and React Query.

The dashboard provides an interactive interface for testing RAG pipelines, visualizing evaluations, monitoring documents, and comparing pipeline performance in real time.

## Features Implemented
### 1. Query Playground (/playground)

Interactive RAG query interface with streaming responses.

Features

Pipeline selector dropdown
Query input with live character counter
Compare mode toggle
Side-by-side pipeline comparison UI
Streaming SSE response support
Citation chips
Citation side drawer
Feedback buttons (👍 / 👎)
Evaluation metric score bars
Async evaluation visualization

Streaming Support

Implemented using:

Server Sent Events (SSE)
Custom React hook: useSSEStream

Streaming tokens appear progressively instead of rendering all at once.
---

### 2. Pipeline Manager (/pipelines)
   
Pipeline visualization and analytics dashboard.

Features
Pipeline cards
Version display
Average evaluation scores
Query statistics
Pipeline health visualization
JSON pipeline editor support
Analytics visualization placeholders
---

### 3. Evaluation Feed (/evaluations)
   
Real-time evaluation monitoring dashboard.

Features
Live evaluation feed
SSE event handling
Evaluation cards
Metric visualization
Query monitoring UI
Pipeline filtering support
---

### 4. Documents Dashboard (/documents)
Document ingestion and chunk monitoring interface.

Features
Drag-and-drop upload zone
Multiple file upload support
File status table
Animated processing badge
Chunk count visualization
Similar chunk search button
Upload metadata display
---

## Tech Stack
Frontend
Next.js 14
TypeScript
Tailwind CSS
React Query
Axios
Zustand
Recharts
Monaco Editor

Backend Integration
FastAPI
SSE Streaming
Redis Pub/Sub
PostgreSQL
MLflow 

## 🧩 Folder Structure
```
frontend/
│
├── src/
│   ├── app/
│   │   ├── playground/
│   │   ├── pipelines/
│   │   ├── evaluations/
│   │   └── documents/
│   │
│   ├── hooks/
│   │   └── useSSEStream.ts
│   │
│   └── components/
│
├── public/
├── package.json
└── tsconfig.json

```

## Installed Packages
```
npm install @tanstack/react-query axios zustand recharts @xyflow/react @monaco-editor/react
```


## Running the Frontend
Start Next.js
```
cd frontend
npm install
npm run dev
```
Frontend runs at:
```
http://localhost:3000
```
## Backend Requirements

Ensure backend services are running:
```
cd infra
docker compose up -d
```
Then run FastAPI backend:
```
cd backend
source venv/Scripts/activate
python -m uvicorn main:app --reload
```
Backend runs at:
```
http://127.0.0.1:8000
```
## SSE Streaming Verification

Open:
```
http://127.0.0.1:8000/query/abc-123/stream
```
Expected:

Retrieval events
Token-by-token streaming
Final citations payloadts


## Completed Requirements Checklist

 ### Playground
 Streaming token response
 Compare mode
 Citation drawer
 Evaluation gauges
 Feedback buttons
 
### Pipelines
 Pipeline cards
 Score visualization
 Analytics placeholders
 
### Evaluations
 Real-time SSE feed
 Evaluation cards
 Metric visualization

### Documents
 Upload zone
 Processing badge
 Similar chunk search

---

## Git Commands 
```
git add frontend/ backend/
git commit -m "feat: Next.js dashboard with playground, pipeline manager, and evaluation feed"
git push -u origin task-41
```
## Result

Task 11 successfully adds a modern interactive dashboard for NeuroFlow with:

live SSE streaming,
RAG pipeline comparison,
evaluation monitoring,
document visualization,
and frontend analytics support.
