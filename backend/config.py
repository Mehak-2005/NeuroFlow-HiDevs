from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    postgres_url: str
    redis_url: str
    MLFLOW_URL: str

    model_config = SettingsConfigDict(env_file=".env")


settings = Settings()
