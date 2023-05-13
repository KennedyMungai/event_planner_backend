"""The DB connection file"""
from sqlmodel import SQLModel, Session, create_engine
from models.events_model import Event


database_connection_string = "sqlite:///planner.db"
connect_args = {"check_same_thread": False}
engine_url = create_engine(database_connection_string,
                           connect_args=connect_args)


def conn():
    """The db connection function"""
    SQLModel.metadata.create_all(engine_url)


def get_session():
    """The db session function"""
    with Session(engine_url) as session:
        yield session
