


from fastapi import APIRouter , HTTPException
from app.schemas.user_schema import UserCreate
from app.services import user_service




router = APIRouter(prefix="/users", tags=["users"])



@router.get("/")
async def get_users():
    return await user_service.get_all_users()

@router.get("/{user_id}")
async def get_user_by_id(user_id: int):
    user = await user_service.get_user_by_id(user_id)

    if user is None:
        raise HTTPException( status_code=404,  detail="User not found"  )

    return user

@router.post("/")
async def create_user(user: UserCreate):
    return await user_service.create_user(user)


@router.put("/{user_id}")
async def update_user(user_id: int, user: UserCreate):
    update_user = await user_service.update_user(user_id, user)

    if update_user is None:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )
    return update_user

@router.delete("/{user_id}")
async def delete_user(user_id: int):
    deleted_user = await user_service.delete_user(user_id)

    if deleted_user is None:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )

    return {
        "message": "User deleted successfully",
        "deleted_user": deleted_user
    }


@router.post("/{user_id}/register")
async def register_user(user_id: int ):
    registered_user = await user_service.register_user(user_id)

    if registered_user is None:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )

    if registered_user == "already_registered":
        raise HTTPException(
            status_code=409,
            detail="User already registered"
        )

    return {
        "message": "User registered successfully",
        "user" : registered_user
    }