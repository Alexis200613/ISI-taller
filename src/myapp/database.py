import os

from flask import g
from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker

DATABASE_URL = os.environ.get("DATABASE_URL", "sqlite:///isi_taller.db")

engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(bind=engine, autoflush=False, expire_on_commit=False)


class Base(DeclarativeBase):
    pass


def init_db():
    from .models.Category import Category
    from .models.Question import Question

    Base.metadata.create_all(
        bind=engine, tables=[Category.__table__, Question.__table__]
    )


def get_db():
    if "db" not in g:
        g.db = SessionLocal()
    return g.db


def close_db(error=None):
    db = g.pop("db", None)
    if db is not None:
        db.close()
