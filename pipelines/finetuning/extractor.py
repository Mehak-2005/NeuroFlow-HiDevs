import json
import re
import uuid
from pathlib import Path

PII_REGEX = r"(\\b\\d{10}\\b|[\\w.-]+@[\\w.-]+)"

training_pairs = [
    {
        "query": "What is AI?",
        "answer": "Artificial intelligence is simulation of human intelligence. [Source 1]",
        "context": "AI refers to simulation of human intelligence.",
        "quality_score": 0.9,
        "user_rating": 5
    }
] * 10


def validate_pair(pair):
    if pair["quality_score"] < 0.82:
        return False

    if pair["user_rating"] is not None and pair["user_rating"] < 4:
        return False

    if re.search(PII_REGEX, pair["query"]):
        return False

    if "[Source" not in pair["answer"]:
        return False

    if len(pair["answer"]) < 50:
        return False

    return True


def extract_training_data():
    job_id = str(uuid.uuid4())

    output_path = Path(f"../training_data/{job_id}.jsonl")

    valid_pairs = []

    with open(output_path, "w") as f:
        for pair in training_pairs:
            if validate_pair(pair):

                data = {
                    "messages": [
                        {
                            "role": "system",
                            "content": "You are a precise research assistant."
                        },
                        {
                            "role": "user",
                            "content": f"[Context]\\n{pair['context']}\\n[Question]\\n{pair['query']}"
                        },
                        {
                            "role": "assistant",
                            "content": pair["answer"]
                        }
                    ]
                }

                f.write(json.dumps(data) + "\\n")
                valid_pairs.append(pair)

    return job_id, output_path, valid_pairs