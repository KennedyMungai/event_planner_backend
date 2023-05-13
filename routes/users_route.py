"""The users route"""
from fastapi import APIRouter, HTTPException, status

from models.users_model import User, UserSignIn

from database.connection import Database

user_database = Database(User)

user_router = APIRouter(
    tags=["User"],
)

users = {}


@user_router.post("/signup")
async def sign_user_up(data: User) -> dict:
    """The endpoint for signing up a user

    Args:
        data (User): The user data

    Raises:
        HTTPException: A 409 is raised if the email already exists

    Returns:
        dict: A message to show a successful sign up
    """
    if data.email in users:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="User with supplied username exists"
        )

    users[data.email] = data

    return {
        "message": "User successfully registered!"
    }


@user_router.post("/signin")
async def sign_user_in(user: UserSignIn) -> dict:
    """An endpoint to show a successful signin

    Args:
        user (UserSignIn): The user object

    Raises:
        HTTPException: A 404 is raised if the user is not found
        HTTPException: A 403 is raised if the user enters the wrong password

    Returns:
        dict: _description_
    """
    user_exist = await User.find_one(User.email == user.email)

    if not user_exist:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User with supplied username not found"
        )

    if user_exist.password != user.password:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials passed")
