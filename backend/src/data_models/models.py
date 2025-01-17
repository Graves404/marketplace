import datetime
from typing import Annotated
from sqlalchemy.orm import declarative_base, Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey, text, String

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

    images: Mapped[list["Images"]] = relationship(back_populates="items")

class Images(Base):
    __tablename__ = "url_photo_items"

    id: Mapped[intpk]
    file_name: Mapped[str] = mapped_column(String(500))
    url_photo: Mapped[str] = mapped_column(String(500))
    items_id: Mapped[int] = mapped_column(ForeignKey("items.id", ondelete="CASCADE"))

    items: Mapped["Items"] = relationship(back_populates="images")

