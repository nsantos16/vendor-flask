from pydantic import BaseSettings


class Settings(BaseSettings):
    database_user: str
    database_password: str
    database_name: str


settings = Settings()
