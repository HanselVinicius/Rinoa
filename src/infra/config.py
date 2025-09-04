import os

from dotenv import load_dotenv

load_dotenv()


class Settings:
    PROJECT_NAME: str = "FastAPI Project"
    PROJECT_VERSION: str = "0.1.0"
    DATABASE_URL: str = os.getenv(
        "DATABASE_URL",
        "postgresql+asyncpg://default_user:default_password@localhost:5432/RinoaDb",
    )


settings = Settings()
