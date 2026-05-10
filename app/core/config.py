from pydantic_settings import BaseSettings

class Settings(BaseSettings):

    PROJECT_NAME: str = "Production Tech Docs Q&A API"
   
    class Config:
        env_file = ".env"

settings = Settings()