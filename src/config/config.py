from pydantic_settings import BaseSettings
from dotenv import load_dotenv
from pathlib import Path
from typing import Optional, Tuple



load_dotenv(
    Path(__file__).parent.parent.parent / ".env"
)


class Settings(BaseSettings):

    GROQ_API_KEY: str 
    DATA_BASE: str
    FIRECRAWL_API_KEY: str
    ELEVENLABS_KEY: str
    SECRET_KEY: str 
    ALGORITHM: str 
    ACCESS_TOKEN_EXPIRE_MINUTES: int

    class config:

        env_file=".env"


settings = Settings()                

