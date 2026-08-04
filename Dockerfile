FROM python:3.11

WORKDIR /app

COPY --from=ghcr.io/astral-sh/uv:latest /uv /usr/local/bin/uv

COPY pyproject.toml uv.lock ./
COPY . .

RUN uv sync --frozen --no-dev

ENTRYPOINT ["uv", "run", "tree-exporter"]