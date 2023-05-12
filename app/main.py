"""The main file for the application"""
from fastapi import FastAPI


app = FastAPI(
    title="Event Planner Backend",
    description="A simple backend for an event planner"
)
