import random

from locust import HttpUser, between, task

SAMPLE_QUERIES = ["What is AI?", "Explain transformers", "What is RAG?"]


class QueryUser(HttpUser):
    host = "http://localhost:8000"

    wait_time = between(1, 2)

    weight = 7

    @task
    def query_pipeline(self):

        self.client.post("/query", json={"query": random.choice(SAMPLE_QUERIES)})


class IngestUser(HttpUser):
    host = "http://localhost:8000"

    wait_time = between(2, 5)

    weight = 2

    @task
    def ingest_document(self):

        with open("tests/fixtures/test_doc.pdf", "rb") as f:
            self.client.post("/ingest", files={"file": f})


class AdminUser(HttpUser):
    host = "http://localhost:8000"

    wait_time = between(3, 5)

    weight = 1

    @task
    def check_evaluations(self):

        self.client.get("/evaluations")
