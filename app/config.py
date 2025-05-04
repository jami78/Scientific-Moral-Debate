from pydantic_settings import BaseSettings
from dotenv import load_dotenv

class Settings(BaseSettings):
    OPENAI_API_KEY: str


def get_settings() -> Settings:
    load_dotenv(override=True)
    return Settings()

get_settings()
