"""The events route file"""
from typing import List

from fastapi import APIRouter, Body, HTTPException, status

from models.events_model import Event


event_router = APIRouter(prefix="/events", tags=["Events"])

events = []


@event_router.get("/", response_model=List[Event])
async def retrieve_all_events() -> List[Event]:
    """Retrieve all events"""
    return events
