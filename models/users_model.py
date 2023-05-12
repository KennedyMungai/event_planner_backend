"""The model for the users data"""
from typing import List, Optional

from pydantic import BaseModel, EmailStr

from models.events_model import Event


class User(BaseModel):
    """The model for the user data

    Args:
        BaseModel (pydantic): The parent class for the User class
    """
    email: EmailStr
    password: str
    events: Optional[List[Event]]

    class Config:
        """The config for the User class"""
        schema_extra = {
            "example": {
                "email": "fastapi@packt.com",
                "username": "strong!!!",
                "events": [],
            }
        }
