'''
=========
config.py
=========

'''

from pydantic_settings import BaseSettings, SettingsConfigDict


class Config(BaseSettings):
    APP_NAME: str
    APP_VERSION: str
    APP_ENV: str
    DEBUG: bool

    HOST: str
    PORT: int

    DB_HOST: str
    DB_DRIVE: str
    DB_PORT: int
    DB_NAME: str
    DB_USER: str
    DB_PASSWORD: str

    @property
    def DATABASE_URL(self):
        return f'{self.DB_DRIVE}://{self.DB_USER}:{self.DB_PASSWORD}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}'

    JWT_SECRET_KEY: str
    JWT_ALGORITHM: str

    ACCESS_TOKEN_EXPIRE_MINUTES: int
    REFRESH_TOKEN_EXPIRE_DAYS: int

    PASSWORD_HASH_ALGORITHM: str

    BACKEND_CORS_ORIGINS: str

    LOG_LEVEL: str = 'INFO'

    REDIS_HOST: str
    REDIS_PORT: int
    REDIS_DB: int
    REDIS_PASSWORD: str

    TIME_ZONE: str

    model_config = SettingsConfigDict(
        env_file='.env'
    )

config = Config()