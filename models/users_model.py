"""The model for the users data"""
from typing import Optional, List
from beanie import Document, Link

from pydantic import BaseModel, EmailStr

from models.events_model import Event


class User(Document):
    """The template for the User data

    Args:
        Document (Beanie): The parent class for the User data
    """
    email: EmailStr
    password: str
    events: Optional[List[Link[Event]]]

    class Settings:
        """The settings for the User data"""
        name = "users"

    class Config:
        """The configuration subclass for the User data
        """
        schema_extra = {
            "example": {
                "email": "kijana@mangaa.com",
                "password": "kijana123",
                "events": []
            }
        }
