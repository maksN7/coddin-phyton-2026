# Dev Evidence

Ця папка навмисно є тільки в гілці `dev`.

## Підписані скріни по лабораторних

| Лаба | Скрін | Що підтверджує |
| --- | --- | --- |
| Лаба 1 | `screenshot_git_log.png` | Git-гілки та коміти по лабораторних |
| Лаба 2 | `screenshot_docker_containers.png` | Запущені контейнери FastAPI та PostgreSQL |
| Лаба 2 | `screenshot_container_libraries.png` | Встановлені бібліотеки всередині API-контейнера через Poetry |
| Лаба 3 | `screenshot_fastapi_routes_lab3.png` | CRUD-роутери FastAPI з OpenAPI |
| Лаба 4 | `screenshot_postgres_tables.png` | Таблиці PostgreSQL після Alembic міграцій |
| Лаба 4 | `screenshot_postgres_seed_data.png` | Дані, записані в PostgreSQL таблиці |
| Лаба 5 | `screenshot_api_postman_style.png` | JWT login та перевірка GET/POST/PUT/DELETE запитів |

## Текстові докази

- `git_log.txt` — історія Git-комітів по лабораторних.
- `docker_containers.txt` — статус Docker-контейнерів.
- `container_libraries.txt` — список бібліотек у контейнері.
- `fastapi_routes.txt` — список API routes з OpenAPI.
- `postgres_tables.txt` і `postgres_seed_data.txt` — структура та seed-дані БД.
- `api_postman_style_verification.json` — перевірка JWT та CRUD-запитів.
- `lab_command_sequence.txt` — послідовність команд, використаних для виконання лабораторних.

Swagger UI доступний після запуску: `http://localhost:8000/docs`.
