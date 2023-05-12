"""The Users route file"""
from fastapi import APIRouter, HTTPException, status
from models.users_model import User, UserSignIn

user_router = APIRouter(prefix="/users", tags=["users"])


users = {}


@user_router.post("/signup", status_code=status.HTTP_201_CREATED)
async def sign_new_user(_data: UserSignIn) -> dict:
    """The endpoint to create a new user

    Args:
        _data (UserSignIn): The data used to create a new user

    Raises:
        HTTPException: A 409 is raised if t

    Returns:
        dict: _description_
    """
    if _data.email in users:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="User already exists",
        )

    users[_data.email] = _data

    return {"message": "User created successfully"}
