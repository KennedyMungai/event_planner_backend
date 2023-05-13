"""The events model class"""
from typing import List, Optional

from beanie import Document
from pydantic import BaseModel


class Event(Document):
    """The template for the Event data

    Args:
        Document (Document): The beanie document class
    """
    title: str
    image: str
    description: str
    tags: List[str]
    location: str

    class Config:
        """The Event configuration subclass
        """
        schema_extra = {
            "example": {
                "title": "Kijana Mang'aa",
                "image": "https://www.kijana.com/wp-content/uploads/2019/12/Kijana-Mang'aa-2.jpg",
                "description": "Kijana Mang'aa is a traditional Thai food event that is held in the city of Bangkok.",
                "tags": ["Thai", "Food", "Bakery"],
                "location": "Bangkok"
            }
        }

    class Settings:
        """The Settings subclass for the Event model
        """
        name = "events"


class EventUpdate(BaseModel):
    """The template for the update data

    Args:
        BaseModel (Pydantic): The base class for the EventUpdate class
    """
    title: Optional[str]
    image: Optional[str]
    description: Optional[str]
    tags: Optional[List[str]]
    location: Optional[str]

    class Config:
        """The subclass for the EventUpdate class
        """
        schema_extra = {
            "example": {
                "title": "Kijana Mang'aa",
                "image": "https://www.kijana.com/wp-content/uploads/2019/12/Kijana-Mang'aa-2.jpg",
                "description": "Kijana Mang'aa is a traditional Thai food event that is held in the city of Bangkok.",
                "tags": ["Thai", "Food", "Bakery"],
                "location": "Bangkok"
            }
        }
