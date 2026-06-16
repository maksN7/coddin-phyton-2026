# FastAPI Labs

Навчальний проєкт для лабораторних робіт 1-5:

- Poetry замість pip для керування залежностями./
- FastAPI з роутерами та Pydantic-схемами.
- Docker Compose: API-контейнер з autoreload і PostgreSQL.
- Async SQLAlchemy, Alembic міграції, seed-дані.
- CRUD для users, profiles, categories, products, orders.
- Реєстрація, login, JWT access token у cookie та Bearer token.

## Запуск

```powershell
docker compose up --build
```

Документація API: http://localhost:8000/docs

## Міграції

```powershell
docker compose exec api poetry run alembic upgrade head
```

## Seed-дані

Seed виконується при старті контейнера через `entrypoint.sh`.
