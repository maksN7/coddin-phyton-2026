from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload

from app.models.order import Order, OrderItem
from app.models.product import Product
from app.schemas.order import OrderCreate, OrderUpdate


async def get_order(db: AsyncSession, order_id: int) -> Order | None:
    result = await db.execute(select(Order).options(selectinload(Order.items)).where(Order.id == order_id))
    return result.scalar_one_or_none()


async def list_orders(db: AsyncSession, skip: int = 0, limit: int = 100) -> list[Order]:
    result = await db.execute(select(Order).options(selectinload(Order.items)).offset(skip).limit(limit))
    return list(result.scalars().all())


async def create_order(db: AsyncSession, order_in: OrderCreate) -> Order:
    order = Order(user_id=order_in.user_id)
    db.add(order)
    await db.flush()
    for item_in in order_in.items:
        product = await db.get(Product, item_in.product_id)
        if product is None:
            raise ValueError(f"Product {item_in.product_id} not found")
        db.add(
            OrderItem(
                order_id=order.id,
                product_id=product.id,
                quantity=item_in.quantity,
                unit_price=product.price,
            )
        )
    await db.commit()
    return await get_order(db, order.id)


async def update_order(db: AsyncSession, order: Order, order_in: OrderUpdate) -> Order:
    order.status = order_in.status
    await db.commit()
    return await get_order(db, order.id)


async def delete_order(db: AsyncSession, order: Order) -> None:
    await db.delete(order)
    await db.commit()
