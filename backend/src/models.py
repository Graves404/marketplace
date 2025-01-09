import datetime
from typing import Annotated
from sqlalchemy.orm import declarative_base, Mapped, mapped_column 
from sqlalchemy import ForeignKey, text

Base = declarative_base()

intpk = Annotated[int, mapped_column(primary_key=True, autoincrement=True)]

class User(Base):
    __tablename__ = 'users'

    id: Mapped[intpk]
    name: Mapped[str]
    surname: Mapped[str]
    email: Mapped[str]
    city: Mapped[str]
    phone: Mapped[str]


class Items(Base):
    __tablename__ = "items"

    id: Mapped[intpk]
    title : Mapped[str]
    description : Mapped[str | None]
    price : Mapped[int | None]
    city : Mapped[str | None]
    user_id : Mapped[int] = mapped_column(ForeignKey("users.id", ondelete="CASCADE"))
    created_at: Mapped[datetime.datetime] = mapped_column(server_default = text("TIMEZONE('utc', now())"))



