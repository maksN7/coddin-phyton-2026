# Environment Setup

Create a local `.env` file from `.env.example` before starting Docker Compose.

Example for local lab testing:

```env
APP_NAME=FastAPI Labs
APP_ENV=dev
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres
POSTGRES_DB=fastapi_labs
POSTGRES_HOST_PORT=55432
DATABASE_URL=postgresql+asyncpg://postgres:postgres@db:5432/fastapi_labs
JWT_SECRET_KEY=local-dev-secret
JWT_ALGORITHM=HS256
JWT_EXPIRE_MINUTES=60
```

The `.env` file is ignored by Git and should not be committed.
