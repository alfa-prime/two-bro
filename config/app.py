from pydantic import BaseSettings, Field


class Settings(BaseSettings):
    ds_bot_token: str = Field(..., env="DS_BOT_TOKEN")
    py_bot_token: str = Field(..., env="PY_BOT_TOKEN")
    bot_id: str = 'TEST VALUES'

    log_level: str = Field(..., env="LOG_LEVEL")
    log_output: str = Field(..., env="LOG_OUTPUT")

    class Config:
        env_file = './.env'
        env_file_encoding = "utf-8"


settings = Settings()