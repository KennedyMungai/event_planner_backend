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
