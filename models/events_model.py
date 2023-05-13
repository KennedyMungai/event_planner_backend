"""The events model class"""
from beanie import Document
from typing import Optional, List


class Event(Document):
    title: str
    image: str
    description: str
    tags: List[str]
    location: str

    class Config:
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
        name = "events"
