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


@event_router.get("/{_event_id}", response_model=Event)
async def retrieve_single_event(_event_id: int) -> Event:
    """Retrieve a single event"""
    for event in events:
        if event.id == _event_id:
            return event
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Event with the given id does not exist",
    )


@event_router.post("/new", status_code=status.HTTP_201_CREATED)
async def create_event(_body: Event = Body(...)) -> dict[str, str]:
    """Create a new event"""
    events.append(_body)
    return {"message": "Event successfully created"}


@event_router.delete("/{_id}")
async def delete_event(_id: int) -> dict:
    """The endpoint to delete a single event

    Args:
        id (int): The id of the event

    Raises:
        HTTPException: A 404 is raised if the event is not found

    Returns:
        dict: A message to show successful deletion of an event
    """
    for event in events:
        if event.id == _id:
            events.remove(event)
            return {"message": "Event successfully deleted"}

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Event with the given id does not exist",
    )


@event_router.delete("/")
async def delete_all_events() -> dict:
    """The endpoint to delete all events

    Returns:
        dict: A message to show successful deletion of all events
    """
    events.clear()

    return {"message": "All events successfully deleted"}
