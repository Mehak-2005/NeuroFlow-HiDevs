def check_queue_depth(queue_depth):

    if queue_depth > 100:
        return {
            "status": 503,
            "error": "ingestion_queue_full",
            "queue_depth": queue_depth,
            "retry_after": 30,
        }

    elif queue_depth > 50:
        return {"status": 202, "warning": "high_queue_depth", "estimated_wait_minutes": 5}

    return {"status": 200, "message": "ok"}
