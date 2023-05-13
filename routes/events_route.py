"""The events route file"""
from fastapi import APIRouter, Depends, HTTPException, Request, status
from database.connection import get_session
from models.events_model import Event, EventUpdate


events_route = APIRouter(prefix="/events", tags=["Events"])


@events_route.post("/new")
async def create_event(new_event: Event, session=Depends(get_session)) -> dict[str, str]:
    """Creates a new event"""
    session.add(new_event)
    session.commit()
    session.refresh(new_event)

    return {"message": "Event created successfully"}
