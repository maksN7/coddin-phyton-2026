import asyncio
from decimal import Decimal

from sqlalchemy import select

from app.core.security import hash_password
from app.db.session import async_session_factory
from app.models.category import Category
from app.models.order import Order, OrderItem
from app.models.product import Product
from app.models.profile import Profile
from app.models.user import User


async def seed() -> None:
    async with async_session_factory() as db:
        result = await db.execute(select(User).limit(1))
        if result.scalar_one_or_none():
            return

        admin = User(email="admin@example.com", username="admin", hashed_password=hash_password("admin12345"))
        customer = User(email="customer@example.com", username="customer", hashed_password=hash_password("customer12345"))
        db.add_all([admin, customer])
        await db.flush()

        db.add_all(
            [
                Profile(user_id=admin.id, full_name="Admin User", phone="+380000000001", address="Kyiv"),
                Profile(user_id=customer.id, full_name="Customer User", phone="+380000000002", address="Lviv"),
            ]
        )

        books = Category(name="Books", description="Educational books and manuals")
        tech = Category(name="Tech", description="Small useful tech products")
        db.add_all([books, tech])
        await db.flush()

        notebook = Product(category_id=books.id, name="FastAPI Workbook", description="Practice book", price=Decimal("25.50"), stock=15)
        keyboard = Product(category_id=tech.id, name="Compact Keyboard", description="USB-C keyboard", price=Decimal("49.99"), stock=8)
        db.add_all([notebook, keyboard])
        await db.flush()

        order = Order(user_id=customer.id, status="paid")
        db.add(order)
        await db.flush()
        db.add_all(
            [
                OrderItem(order_id=order.id, product_id=notebook.id, quantity=1, unit_price=notebook.price),
                OrderItem(order_id=order.id, product_id=keyboard.id, quantity=1, unit_price=keyboard.price),
            ]
        )
        await db.commit()


if __name__ == "__main__":
    asyncio.run(seed())
