# -*- coding: utf-8 -*-
from functools import lru_cache
from pathlib import Path
import os


BASEDIR = Path(__file__).parent.resolve()


class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY", "very_hard_key")
    POSTGRES_DB = os.environ.get("POSTGRES_DB", "db")
    POSTGRES_PORT = os.environ.get("POSTGRES_PORT", 15432)
    POSTGRES_USER = os.environ.get("POSTGRES_USER", "postgres")
    POSTGRES_HOST = os.environ.get("POSTGRES_HOST", "localhost")
    POSTGRES_PASSWORD = os.environ.get("POSTGRES_PASSWORD", "postgres")
    SQLALCHEMY_DATABASE_URI = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}"


@lru_cache
def get_config() -> Config:
    return Config()
