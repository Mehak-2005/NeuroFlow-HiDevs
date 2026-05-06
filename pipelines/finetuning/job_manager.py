import asyncio
import uuid

async def submit_finetune_job(jsonl_path, base_model):

    await asyncio.sleep(2)

    return f"ft-job-{uuid.uuid4()}"