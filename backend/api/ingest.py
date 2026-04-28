from fastapi import APIRouter, UploadFile, File
import shutil
import uuid

router = APIRouter()

@router.post("/ingest")
async def ingest(file: UploadFile = File(...)):
    file_id = str(uuid.uuid4())
    path = f"uploads/{file_id}_{file.filename}"

    with open(path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    return {
        "document_id": file_id,
        "status": "queued",
        "duplicate": False
    }