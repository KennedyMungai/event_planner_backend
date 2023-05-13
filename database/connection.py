"""The DB connection file"""
from typing import Optional

from beanie import init_beanie
from motor.motor_asyncio import AsyncIOMotorClient
from pydantic import BaseSettings
import os
from dotenv import find_dotenv, load_dotenv


load_dotenv(find_dotenv())


DATABASE_URL = os.environ.get("DATABASE_URL")


class Settings(BaseSettings):
    """The settings class for the model

    Args:
        BaseSettings (pydantic): Pydantic Base Settings
    """
    async def initialize_database(self):
        """The function to initialize a database connection"""
        client = AsyncIOMotorClient(self.DATABASE_URL)
        await init_beanie(database=client.events, document_models=[])
