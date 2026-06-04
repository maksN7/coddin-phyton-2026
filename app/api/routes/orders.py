from fastapi import APIRouter, HTTPException, status

from app.api.deps import CurrentUser, DbSession
from app.crud import orders as crud_orders
from app.schemas.order import OrderCreate, OrderRead, OrderUpdate

router = APIRouter()


@router.get("/", response_model=list[OrderRead])
async def list_orders(db: DbSession, current_user: CurrentUser, skip: int = 0, limit: int = 100):
    return await crud_orders.list_orders(db, skip, limit)


@router.get("/{order_id}", response_model=OrderRead)
async def get_order(order_id: int, db: DbSession, current_user: CurrentUser):
    order = await crud_orders.get_order(db, order_id)
    if order is None:
        raise HTTPException(status_code=404, detail="Order not found")
    return order


@router.post("/", response_model=OrderRead, status_code=status.HTTP_201_CREATED)
async def create_order(order_in: OrderCreate, db: DbSession, current_user: CurrentUser):
    try:
        return await crud_orders.create_order(db, order_in)
    except ValueError as exc:
        raise HTTPException(status_code=400, detail=str(exc)) from exc


@router.put("/{order_id}", response_model=OrderRead)
async def update_order(order_id: int, order_in: OrderUpdate, db: DbSession, current_user: CurrentUser):
    order = await crud_orders.get_order(db, order_id)
    if order is None:
        raise HTTPException(status_code=404, detail="Order not found")
    return await crud_orders.update_order(db, order, order_in)


@router.delete("/{order_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_order(order_id: int, db: DbSession, current_user: CurrentUser):
    order = await crud_orders.get_order(db, order_id)
    if order is None:
        raise HTTPException(status_code=404, detail="Order not found")
    await crud_orders.delete_order(db, order)
