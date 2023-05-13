"""The DB connection file"""
from typing import Optional

from beanie import init_beanie
from motor.motor_asyncio import AsyncIOMotorClient
from pydantic import BaseSettings


class Settings(BaseSettings):
    """The settings class for the model

    Args:
        BaseSettings (pydantic): Pydantic Base Settings
    """
    DATABASE_URL: Optional[str] = None

    async def initialize_database(self):
        """The function to initialize a database connection"""
        client = AsyncIOMotorClient(self.DATABASE_URL)
        await init_beanie(database=client.events, document_models=[])

    class Config:
        """The configuration subclass for the Settings class"""
        env_file = "../.env"
