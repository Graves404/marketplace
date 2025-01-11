from config import settings
from sqlalchemy import create_engine, text, select
from sqlalchemy.orm import sessionmaker, DeclarativeBase
from typing import Annotated


engine = create_engine(
        url=settings.DATABASE_URL_psycopg,
        echo=False,
        pool_size=5,
        max_overflow=10
        )

session_factory = sessionmaker(engine)

str_256 = Annotated[str, 256]

class Base(DeclarativeBase):
    pass

