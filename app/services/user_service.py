

from app.schemas.user_schema import UserCreate
from app.repositories import user_repository
from datetime import date
import httpx
from app.config import Config

async def get_all_users():
    return await user_repository.get_all_users()

async def create_user(user: UserCreate):
    user_data = user.model_dump()

    user_data["joining_date"] = date.today()
    user_data["is_registered"] = False


    user_id = await user_repository.save_user(user_data)

    return{
        "message": "User created successfully",
        "user_id": user_id,
        "user": user_data
    }

async def get_user_by_id(user_id: int):
    return await user_repository.get_user_by_id(user_id)

async def update_user( user_id: int, user: UserCreate):
    existing_user = await user_repository.get_user_by_id(user_id)

    if existing_user is None:
       return None

    user_data = user.model_dump()

    user_data["joining_date"] = existing_user["joining_date"]
    user_data["is_registered"] = existing_user["is_registered"]

    updated_user = await user_repository.update_user(user_id, user_data)

    return updated_user



async def delete_user(user_id: int):

    existing_user = await user_repository.get_user_by_id(user_id)

    if existing_user is None:
        return None

    await delete_user_votes(user_id)

    deleted_user = await user_repository.delete_user(user_id)

    return deleted_user




async def register_user(user_id: int):
    user = await user_repository.get_user_by_id(user_id)

    if user is None:
        return None

    if user["is_registered"]:
        return "User already registered"

    return await user_repository.register_user(user_id)


async def delete_user_votes(user_id: int):
    url = f"{Config().POLL_SERVICE_URL}/users/{user_id}/votes"

    async with httpx.AsyncClient(timeout=10.0) as client:
        response = await client.delete(url)

        response.raise_for_status()

    return True