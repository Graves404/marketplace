import datetime
from typing import Annotated
from sqlalchemy.orm import declarative_base, Mapped, mapped_column
from sqlalchemy import ForeignKey, text

Base = declarative_base()


class User(Base):
    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    surname: Mapped[str]
    email: Mapped[str]
    city: Mapped[str]
    phone: Mapped[str]


class Items(Base):
    __tablename__ = "items"

    id: Mapped[int] = mapped_column(primary_key=True)
    title : Mapped[str]
    description : Mapped[str | None]
    price : Mapped[int]
    city : Mapped[str]
    id_user : Mapped[int] = mapped_column(ForeignKey("user.id", ondelete="CASCADE"))
    data_create : Mapped[datetime.datetime] = mapped_column(server_default = text("TIMEZONE('utc', now())"))



