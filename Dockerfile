FROM python:3.11

COPY --from=ghcr.io/astral-sh/uv:latest /uv /usr/local/bin/uv

WORKDIR /opt/tree-exporter

COPY pyproject.toml uv.lock ./
COPY src ./src
COPY README.md LICENSE ./

RUN uv sync --frozen --no-dev

WORKDIR /github/workspace

ENTRYPOINT ["/opt/tree-exporter/.venv/bin/tree-exporter"]
