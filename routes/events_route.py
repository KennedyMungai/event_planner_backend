"""The events route file"""
from typing import List

from fastapi import APIRouter, Depends, HTTPException, Request, status
from sqlmodel import select

from database.connection import get_session
from models.events_model import Event, EventUpdate

events_router = APIRouter(prefix="/events", tags=["Events"])


@events_router.post(
    "/new",
    name="Create Post",
    description="The endpoint to create a new post",
    status_code=status.HTTP_201_CREATED
)
async def create_event(new_event: Event, session=Depends(get_session)) -> dict[str, str]:
    """Creates a new event"""
    session.add(new_event)
    session.commit()
    session.refresh(new_event)

    return {"message": "Event created successfully"}


@events_router.get("/", response_model=List[Event])
async def retrieve_all_events(session=Depends(get_session)) -> List[Event]:
    """Retrieves all events"""
    statement = select(Event)
    events = session.exec(statement).all()
    return events


@events_router.get("/{id}", response_model=Event)
async def retrieve_event(id: int, session=Depends(get_session)) -> Event:
    """Retrieves an event"""
    event = session.get(Event, id)

    if (event):
        return event

    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                        detail=f"Event with {id} not found"
                        )


@events_router.put("/edit/{id}", response_model=Event)
async def edit_event(id: int, event_update: EventUpdate,
                     session=Depends(get_session)) -> Event:
    """Edits an event"""
    event = session.get(Event, id)

    if event:
        event_data = event_update.dict(exclude_unset=True)
        for key, value in event_data.items():
            setattr(event, key, value)

        session.add(event)
        session.commit()
        session.refresh(event)

        return event

    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                        detail=f"Event with id {id} not found")
