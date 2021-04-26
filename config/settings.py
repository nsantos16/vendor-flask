from pydantic import BaseSettings


class Settings(BaseSettings):
    # Database settings
    database_user: str = "postgres"
    database_password: str = "postgres"
    database_name: str = "vend_o_matic"
    database_host: str = "127.0.0.1"

    # Testing database
    test_database_user: str = "postgres"
    test_database_password: str = "postgres"
    test_database_name: str = "vend_testing"
    test_database_host: str = "127.0.0.1"

    # Feature flags
    feat_flag_more_than_one_coin: bool = False


settings = Settings()
