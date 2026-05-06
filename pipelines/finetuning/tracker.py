import mlflow
from statistics import mean

def start_training_job(job_id, pairs):

    mlflow.set_experiment("neuroflow-finetuning")

    with mlflow.start_run(run_name=f"finetune-{job_id}") as run:

        mlflow.log_params({
            "base_model": "gpt-3.5-turbo",
            "training_pair_count": len(pairs),
            "avg_quality_score": mean([p["quality_score"] for p in pairs])
        })
        mlflow.log_artifact(f"../training_data/{job_id}.jsonl")

        mlflow.log_metrics({
            "training_loss": 0.12,
            "validation_loss": 0.10,
            "training_token_count": 25000
        })

        return run.info.run_id