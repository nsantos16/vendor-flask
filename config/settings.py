from pydantic import BaseSettings


class Settings(BaseSettings):
    # Database settings
    database_user: str
    database_password: str
    database_name: str
    database_host: str = "127.0.0.1"

    # Feature flags
    feat_flag_more_than_one_coin: bool = False


settings = Settings()
