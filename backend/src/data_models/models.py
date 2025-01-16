import datetime
from typing import Annotated
from sqlalchemy.orm import declarative_base, Mapped, mapped_column, relationship
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
    username: Mapped[str]
    hash_pass: Mapped[str]

    items: Mapped[list["Items"]] = relationship(back_populates="user")



class Items(Base):
    __tablename__ = "items"

    id: Mapped[intpk]
    title: Mapped[str]
    description: Mapped[str | None]
    price: Mapped[int | None]
    city: Mapped[str | None]
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id", ondelete="CASCADE"))
    created_at: Mapped[datetime.datetime] = mapped_column(server_default=text("TIMEZONE('utc', now())"))

    user: Mapped["User"] = relationship(back_populates="items")

class Password(Base):
    __tablename__ = "passwords"

    id: Mapped[intpk]
    password: Mapped[str]
    user_id: Mapped[intpk] = mapped_column(ForeignKey("user.id", ondelete="CASCADE"))



