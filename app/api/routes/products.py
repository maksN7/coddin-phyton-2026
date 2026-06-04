from fastapi import APIRouter, HTTPException, status

from app.api.deps import CurrentUser, DbSession
from app.crud.catalog import products
from app.schemas.product import ProductCreate, ProductRead, ProductUpdate

router = APIRouter()


@router.get("/", response_model=list[ProductRead])
async def list_products(db: DbSession, skip: int = 0, limit: int = 100):
    return await products.list(db, skip, limit)


@router.get("/{product_id}", response_model=ProductRead)
async def get_product(product_id: int, db: DbSession):
    product = await products.get(db, product_id)
    if product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    return product


@router.post("/", response_model=ProductRead, status_code=status.HTTP_201_CREATED)
async def create_product(product_in: ProductCreate, db: DbSession, current_user: CurrentUser):
    return await products.create(db, product_in)


@router.put("/{product_id}", response_model=ProductRead)
async def update_product(product_id: int, product_in: ProductUpdate, db: DbSession, current_user: CurrentUser):
    product = await products.get(db, product_id)
    if product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    return await products.update(db, product, product_in)


@router.delete("/{product_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_product(product_id: int, db: DbSession, current_user: CurrentUser):
    product = await products.get(db, product_id)
    if product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    await products.delete(db, product)
