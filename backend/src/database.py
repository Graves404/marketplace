from src.config import settings
from sqlalchemy import create_engine, text, select
from sqlalchemy.orm import sessionmaker, DeclarativeBase
from src.models import User

engine = create_engine(
        url=settings.DATABASE_URL_psycopg,
        echo=False,
        pool_size=5,
        max_overflow=10
        )

session = sessionmaker(engine)

class Base(DeclarativeBase):
    pass

