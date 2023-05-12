"""The events route file"""
from typing import List

from fastapi import APIRouter, Body, HTTPException, status

from models.events_model import Event


event_router = APIRouter(prefix="/events", tags=["Events"])

events = []
