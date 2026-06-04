from fastapi import APIRouter, HTTPException, status

from app.api.deps import CurrentUser, DbSession
from app.crud import users as crud_users
from app.schemas.user import UserCreate, UserRead, UserUpdate

router = APIRouter()


@router.get("/", response_model=list[UserRead])
async def list_users(db: DbSession, current_user: CurrentUser, skip: int = 0, limit: int = 100):
    return await crud_users.list_users(db, skip, limit)


@router.get("/{user_id}", response_model=UserRead)
async def get_user(user_id: int, db: DbSession, current_user: CurrentUser):
    user = await crud_users.get_user(db, user_id)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user


@router.post("/", response_model=UserRead, status_code=status.HTTP_201_CREATED)
async def create_user(user_in: UserCreate, db: DbSession):
    if await crud_users.get_user_by_login(db, user_in.username) or await crud_users.get_user_by_login(db, user_in.email):
        raise HTTPException(status_code=400, detail="User already exists")
    return await crud_users.create_user(db, user_in)


@router.put("/{user_id}", response_model=UserRead)
async def update_user(user_id: int, user_in: UserUpdate, db: DbSession, current_user: CurrentUser):
    user = await crud_users.get_user(db, user_id)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return await crud_users.update_user(db, user, user_in)


@router.delete("/{user_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_user(user_id: int, db: DbSession, current_user: CurrentUser):
    user = await crud_users.get_user(db, user_id)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    await crud_users.delete_user(db, user)
