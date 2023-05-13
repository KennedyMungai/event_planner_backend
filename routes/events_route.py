"""The events route file"""
from typing import List

from beanie import PydanticObjectId
from fastapi import APIRouter, Depends, HTTPException, Request, status
from sqlmodel import select

from database.connection import Database
from models.events_model import Event, EventUpdate

events_router = APIRouter(prefix="/events", tags=["Events"])
event_database = Database(Event)


@events_router.post(
    "/new",
    name="Create Post",
    description="The endpoint to create a new post",
    status_code=status.HTTP_201_CREATED
)
async def create_event(new_event: Event) -> dict[str, str]:
    """Creates a new event"""
    await event_database.create(new_event)

    return {"message": "Event created successfully"}


@events_router.get("/", response_model=List[Event])
async def retrieve_all_events() -> List[Event]:
    """Retrieves all events"""
    events = await event_database.get_all()
    return events


@events_router.get("/{id}", response_model=Event)
async def retrieve_event(_id: PydanticObjectId) -> Event:
    """Retrieves an event"""
    event = await event_database.get(id)

    if not event:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Event with id {id} not found")


@events_router.put("/edit/{id}", response_model=Event)
async def edit_event(_id: PydanticObjectId, event_update: EventUpdate) -> Event:
    """Edits an event"""
    updated_event = await event_database.update(_id, event_update)

    if not updated_event:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Event with the id {id} does not exist")

    return updated_event


@events_router.delete("/delete/{id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_event(_id: int):
    """The endpoint to delete specific events

    Args:
        id (int): The id of the event to be deleted
        session (_type_, optional): The db session. Defaults to Depends(get_session).

    Raises:
        HTTPException: A 404 is raised if the event is not found in the database
    """
    event = await event_database.get(id)

    if not event:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Event with id {id} not found")

    return None
