"""The main file for the application"""
from fastapi import FastAPI


app = FastAPI(
    title="Event Planner Backend",
    description="A simple backend for an event planner"
)


@app.get("/", name="Root", description="The root route for testing",  tags=["Root"])
async def root() -> dict[str, str]:
    """The root route"""
    return {"message": "Hello World"}
