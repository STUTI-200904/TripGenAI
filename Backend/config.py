"""Application configuration loaded from environment variables.

This module keeps secrets and model settings out of the agent code. Set
GROQ_API_KEY in your shell or .env file before calling the planner endpoint.
"""

import os
from dataclasses import dataclass

from dotenv import load_dotenv


load_dotenv()


@dataclass(frozen=True)
class Settings:
    groq_api_key: str | None = os.getenv("GROQ_API_KEY")
    groq_model_name: str = os.getenv("GROQ_MODEL_NAME", "llama-3.3-70b-versatile")
    groq_temperature: float = float(os.getenv("GROQ_TEMPERATURE", "0"))


settings = Settings()
