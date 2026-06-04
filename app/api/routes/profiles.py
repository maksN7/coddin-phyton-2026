from fastapi import APIRouter, HTTPException, status

from app.api.deps import CurrentUser, DbSession
from app.crud.catalog import profiles
from app.schemas.profile import ProfileCreate, ProfileRead, ProfileUpdate

router = APIRouter()


@router.get("/", response_model=list[ProfileRead])
async def list_profiles(db: DbSession, current_user: CurrentUser, skip: int = 0, limit: int = 100):
    return await profiles.list(db, skip, limit)


@router.get("/{profile_id}", response_model=ProfileRead)
async def get_profile(profile_id: int, db: DbSession, current_user: CurrentUser):
    profile = await profiles.get(db, profile_id)
    if profile is None:
        raise HTTPException(status_code=404, detail="Profile not found")
    return profile


@router.post("/", response_model=ProfileRead, status_code=status.HTTP_201_CREATED)
async def create_profile(profile_in: ProfileCreate, db: DbSession, current_user: CurrentUser):
    return await profiles.create(db, profile_in)


@router.put("/{profile_id}", response_model=ProfileRead)
async def update_profile(profile_id: int, profile_in: ProfileUpdate, db: DbSession, current_user: CurrentUser):
    profile = await profiles.get(db, profile_id)
    if profile is None:
        raise HTTPException(status_code=404, detail="Profile not found")
    return await profiles.update(db, profile, profile_in)


@router.delete("/{profile_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_profile(profile_id: int, db: DbSession, current_user: CurrentUser):
    profile = await profiles.get(db, profile_id)
    if profile is None:
        raise HTTPException(status_code=404, detail="Profile not found")
    await profiles.delete(db, profile)
