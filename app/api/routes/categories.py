from fastapi import APIRouter, HTTPException, status

from app.api.deps import CurrentUser, DbSession
from app.crud.catalog import categories
from app.schemas.category import CategoryCreate, CategoryRead, CategoryUpdate

router = APIRouter()


@router.get("/", response_model=list[CategoryRead])
async def list_categories(db: DbSession, skip: int = 0, limit: int = 100):
    return await categories.list(db, skip, limit)


@router.get("/{category_id}", response_model=CategoryRead)
async def get_category(category_id: int, db: DbSession):
    category = await categories.get(db, category_id)
    if category is None:
        raise HTTPException(status_code=404, detail="Category not found")
    return category


@router.post("/", response_model=CategoryRead, status_code=status.HTTP_201_CREATED)
async def create_category(category_in: CategoryCreate, db: DbSession, current_user: CurrentUser):
    return await categories.create(db, category_in)


@router.put("/{category_id}", response_model=CategoryRead)
async def update_category(category_id: int, category_in: CategoryUpdate, db: DbSession, current_user: CurrentUser):
    category = await categories.get(db, category_id)
    if category is None:
        raise HTTPException(status_code=404, detail="Category not found")
    return await categories.update(db, category, category_in)


@router.delete("/{category_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_category(category_id: int, db: DbSession, current_user: CurrentUser):
    category = await categories.get(db, category_id)
    if category is None:
        raise HTTPException(status_code=404, detail="Category not found")
    await categories.delete(db, category)
