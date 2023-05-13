"""The DB connection file"""
from sqlmodel import Session, SQLModel, create_engine

from models.events_model import Event

DATABASE_CONNECTION_STRING = "sqlite:///planner.db"
connect_args = {"check_same_thread": False}
engine_url = create_engine(DATABASE_CONNECTION_STRING,
                           connect_args=connect_args)


def conn():
    """The db connection function"""
    SQLModel.metadata.create_all(engine_url)


def get_session():
    """The db session function"""
    with Session(engine_url) as session:
        yield session
