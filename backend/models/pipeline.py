from pydantic import BaseModel, ConfigDict


class IngestionConfig(BaseModel):
    chunking_strategy: str
    chunk_size_tokens: int
    chunk_overlap_tokens: int
    extractors_enabled: list[str]


class RetrievalConfig(BaseModel):
    dense_k: int
    sparse_k: int
    reranker: str
    top_k_after_rerank: int
    query_expansion: bool
    metadata_filters_enabled: bool


class GenerationConfig(BaseModel):
    model_routing: dict
    max_context_tokens: int
    temperature: float
    system_prompt_variant: str


class EvaluationConfig(BaseModel):
    auto_evaluate: bool
    training_threshold: float


class PipelineConfig(BaseModel):
    model_config = ConfigDict(extra="forbid")  # 🚨 IMPORTANT

    name: str
    description: str
    ingestion: IngestionConfig
    retrieval: RetrievalConfig
    generation: GenerationConfig
    evaluation: EvaluationConfig
