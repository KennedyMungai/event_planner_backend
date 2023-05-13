"""The events route file"""
from fastapi import APIRouter, Depends, HTTPException, Request, status
from database.connection import get_session
from models.events_model import Event, EventUpdate
