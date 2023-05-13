"""The events model class"""
from sqlmodel import JSON, SQLModel, Field, Column
from typing import Optional, List


class Event(SQLModel, table=True):
    """The event model class

    Args:
        SQLModel (Pydantic): The parent class for the models
        table (bool, optional): A bool that defined the model as a table. Defaults to True.
    """
    id: int = Field(default=None, primary_key=True)
    title: str
    image: str
    description: str
    date: str
    tags: List[str] = Field(sa_column=Column(JSON))
    location: str

    class Config:
        """The config subclass for the event class"""
        arbitrary_types_allowed = True
        schema_extra = {
            "example": {
                "title": "SQLite db branch for the event planner code",
                "image": "https://www.w3schools.com/howto/img_avatar.png",
                "description": "This is a description of the event",
                "date": "2022-01-01",
                "tags": ["python", "sql", "sqlite"],
                "location": "Somewhere in the world"
            }
        }
