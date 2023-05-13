"""The main file for the application"""
import uvicorn
from fastapi import FastAPI

from routes.users_route import user_router
from routes.events_route import event_router
from database.connection import conn

app = FastAPI(
    title="Event Planner Backend",
    description="A simple backend for an event planner"
)


@app.get("/", name="Root", description="The root route for testing",  tags=["Root"])
async def root() -> dict[str, str]:
    """The root route"""
    return {"message": "Hello World"}

app.include_router(user_router)
app.include_router(event_router)


if __name__ == "__main__":
    uvicorn.run(app, host="0000000", port=8000)
