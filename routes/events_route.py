"""The events route file"""
from fastapi import APIRouter, Body, HTTPException, status
from models.events_model import Event
from typing import List
