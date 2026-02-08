from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    database_url: str
    environment: str = "development"
    log_level: str = "INFO"
    secret_key: str
    algorithm: str = "HS256"
    access_token_expire_minutes: int = 86400

    class Config:
        env_file = ".env"
        case_sensitive = True

settings = Settings()
