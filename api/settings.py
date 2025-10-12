from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    secret_key: str
    host: str
    port: int

    class Config:
        env_file = '.env'
