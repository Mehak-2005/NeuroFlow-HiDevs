import asyncio

timeouts = {
    "embedding": 10,
    "chat_completion": 60,
    "reranking": 15,
    "evaluation": 120,
    "file_extraction": 30,
    "url_fetch": 15,
}


async def run_with_timeout(task_type, coro):

    timeout = timeouts.get(task_type, 30)

    try:
        return await asyncio.wait_for(coro, timeout=timeout)

    except TimeoutError:
        raise TimeoutError(f"{task_type} timed out")
