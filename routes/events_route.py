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


@event_router.get("/{event_id}", response_model=Event)
async def retrieve_single_event(event_id: int) -> Event:
    """Retrieve a single event"""
    for event in events:
        if event.id == event_id:
            return event
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Event with the given id does not exist",
    )


@event_router.post("/new", status_code=status.HTTP_201_CREATED)
async def create_event(body: Event = Body(...)) -> dict[str, str]:
    """Create a new event"""
    events.append(body)
    return {"message": "Event successfully created"}
