"""The DB connection file"""
import os
from typing import Any, Optional

from beanie import init_beanie, PydanticObjectId
from dotenv import find_dotenv, load_dotenv
from motor.motor_asyncio import AsyncIOMotorClient
from pydantic import BaseModel, BaseSettings

from models.events_model import Event
from models.users_model import User

load_dotenv(find_dotenv())


DATABASE_URL = os.environ.get("DATABASE_URL")


class Settings(BaseSettings):
    """The settings class for the model

    Args:
        BaseSettings (pydantic): Pydantic Base Settings
    """
    async def initialize_database(self):
        """The function to initialize a database connection"""
        client = AsyncIOMotorClient(DATABASE_URL)
        await init_beanie(database=client.events, document_models=[Event, User])


class Database:
    def __init__(self, model):
        self.model = model

    async def save(self, document) -> None:
        await document.create()
        return
