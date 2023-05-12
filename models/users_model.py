"""Users Model"""
from typing import List

from pydantic import BaseModel


class Event(BaseModel):
    """The event model

    Args:
        BaseModel (Pydantic Model): The model for the Event
    """
    id: int
    title: str
    image: str
    description: str
    tags: List[str]
    location: str
