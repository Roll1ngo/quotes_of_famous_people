from pydantic_settings import BaseSettings
from pydantic import ConfigDict


class Settings(BaseSettings):
    SECRET_KEY: str = "Django secret key"

    NAME_DB: str = "name database"
    USER_DB: str = "name user when connect database"
    PASSWORD_DB: str = "password database"
    HOST_DB: str = "host database"
    PORT_DB: int = "port database"

    EMAIL_BACKEND: str = "service for send email"
    EMAIL_HOST: str = "email_host"
    EMAIL_PORT: int = 1111
    EMAIL_STARTTLS: bool = False
    EMAIL_USE_SSL: bool = True
    EMAIL_USE_TLS: bool = False
    EMAIL_HOST_USER: str = "host_user_email"
    EMAIL_HOST_PASSWORD: str = "password_host_user_email"
    DEFAULT_FROM_EMAIL: str = "host_user_email"

    model_config = ConfigDict(extra='ignore', env_file=".env", env_file_encoding="utf-8")


config = Settings()
