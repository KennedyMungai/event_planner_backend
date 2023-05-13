"""The model for the users data"""
from typing import Optional, List
from beanie import Document, Link

from pydantic import BaseModel, EmailStr

from models.events_model import Event


class User(Document):
    email: EmailStr
    password: str
    events: Optional[List[Link[Event]]]

    class Settings:
        name = "users"

    class Config:
        schema_extra = {
            "example": {
                "email": "kijana@mangaa.com",
                "password": "kijana123",
                "events": []
            }
        }
