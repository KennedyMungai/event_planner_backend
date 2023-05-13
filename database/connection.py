"""The DB connection file"""
import os
from typing import Optional

from beanie import init_beanie
from dotenv import find_dotenv, load_dotenv
from motor.motor_asyncio import AsyncIOMotorClient
from pydantic import BaseSettings
from models.users_model import User
from models.events_model import Event

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
