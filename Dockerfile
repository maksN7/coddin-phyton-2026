FROM python:3.12-slim

ENV POETRY_VERSION=1.8.5 \
    POETRY_HOME=/opt/poetry \
    POETRY_NO_INTERACTION=1 \
    POETRY_VIRTUALENVS_CREATE=false \
    PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR /app

RUN apt-get update \
    && apt-get install -y --no-install-recommends curl build-essential libpq-dev \
    && curl -sSL https://install.python-poetry.org | python - \
    && ln -s /opt/poetry/bin/poetry /usr/local/bin/poetry \
    && apt-get purge -y --auto-remove curl \
    && rm -rf /var/lib/apt/lists/*

COPY pyproject.toml README.md ./
RUN poetry install --no-root

COPY . .
RUN chmod +x /app/entrypoint.sh

ENTRYPOINT ["/app/entrypoint.sh"]
