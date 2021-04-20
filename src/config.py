from pydantic import BaseSettings


class Settings(BaseSettings):
    sender_email: str
    sender_password: str
    smtp_server: str
    smtp_port: int

    class Config:
        env_file = "../.env"


settings = Settings()
