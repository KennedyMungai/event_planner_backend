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
