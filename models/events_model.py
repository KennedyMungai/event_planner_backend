"""The events model class"""
from typing import List, Optional

from beanie import Document


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
