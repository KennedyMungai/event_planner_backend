"""The events route file"""
from typing import List

from beanie import PydanticObjectId
from fastapi import APIRouter, Depends, HTTPException, Request, status
from sqlmodel import select

from database.connection import Database, get_session
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
    session.add(new_event)
    session.commit()
    session.refresh(new_event)

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
async def edit_event(_id: int, event_update: EventUpdate) -> Event:
    """Edits an event"""
    event = session.get(Event, _id)

    if event:
        event_data = event_update.dict(exclude_unset=True)
        for key, value in event_data.items():
            setattr(event, key, value)

        session.add(event)
        session.commit()
        session.refresh(event)

        return event

    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                        detail=f"Event with id {_id} not found")


@events_router.delete("/delete/{id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_event(_id: int):
    """The endpoint to delete specific events

    Args:
        id (int): The id of the event to be deleted
        session (_type_, optional): The db session. Defaults to Depends(get_session).

    Raises:
        HTTPException: A 404 is raised if the event is not found in the database
    """
    event = session.get(Event, _id)

    if event:
        session.delete(event)
        session.commit()

        return None

    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                        detail=f"The event with id of {_id} was not found")
