"""The DB connection file"""
import os
from typing import Any, List, Optional

from beanie import PydanticObjectId, init_beanie
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

    async def get(self, id: PydanticObjectId) -> Optional[Any]:
        doc = await self.model.get(id)

        if doc:
            return doc

        return False

    async def get_all(self) -> List[Any]:
        docs = await self.model.find_all()
        return docs

    async def update(self, id: PydanticObjectId, body: BaseModel) -> Any:
        doc_id = id
        des_body = body.dict()
        des_body = {k: v for k, v in des_body.items() if v is not None}
        update_query = {
            "$set": {field: value for field, value in des_body.items()}
        }

        doc = await self.get(doc_id)

        if not doc:
            return False

        await doc.update(update_query)

        return doc
