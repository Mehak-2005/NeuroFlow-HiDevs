from fastapi import APIRouter
from pipelines.finetuning.extractor import extract_training_data
from pipelines.finetuning.job_manager import submit_finetune_job
from pipelines.finetuning.tracker import start_training_job

router = APIRouter()

jobs = []


@router.post("/finetune/jobs")
async def create_job():

    job_id, path, pairs = extract_training_data()

    run_id = start_training_job(job_id, pairs)

    provider_job_id = await submit_finetune_job(str(path), "gpt-3.5-turbo")

    result = {
        "job_id": job_id,
        "mlflow_run_id": run_id,
        "provider_job_id": provider_job_id,
        "pair_count": len(pairs),
        "status": "submitted",
    }

    jobs.append(result)

    return result


@router.get("/finetune/jobs")
async def list_jobs():
    return jobs


@router.get("/finetune/jobs/{job_id}")
async def get_job(job_id: str):

    for job in jobs:
        if job["job_id"] == job_id:
            return job

    return {"error": "job not found"}


@router.get("/finetune/training-data/preview")
async def preview():

    _, _, pairs = extract_training_data()

    return pairs[:5]
