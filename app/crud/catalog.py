from sqlalchemy.ext.asyncio import AsyncSession

from app.crud.base import CRUDBase
from app.models.category import Category
from app.models.product import Product
from app.models.profile import Profile
from app.schemas.category import CategoryCreate, CategoryUpdate
from app.schemas.product import ProductCreate, ProductUpdate
from app.schemas.profile import ProfileCreate, ProfileUpdate

categories = CRUDBase[Category, CategoryCreate, CategoryUpdate](Category)
products = CRUDBase[Product, ProductCreate, ProductUpdate](Product)
profiles = CRUDBase[Profile, ProfileCreate, ProfileUpdate](Profile)


async def ensure_exists(db: AsyncSession, crud: CRUDBase, item_id: int):
    return await crud.get(db, item_id)
