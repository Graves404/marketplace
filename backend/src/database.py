from .settings.config import settings
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase
from typing import Annotated
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker


sync_engine = create_engine(
        url=settings.DATABASE_URL_psycopg,
        echo=False,
        pool_size=5,
        max_overflow=10
        )

async_engine = create_async_engine(
        url=settings.DATABASE_URL_asyncpg,
        echo_pool=False,
        pool_size=5,
        max_overflow=10
)

session_factory = sessionmaker(sync_engine)
async_session_factory = async_sessionmaker(async_engine)

str_256 = Annotated[str, 256]

class Base(DeclarativeBase):
    pass

