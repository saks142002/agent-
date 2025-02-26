FROM python:3.12-slim-bookworm AS builder
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

# Install system dependencies
RUN apt-get update \
    && apt-get install -y --no-install-recommends gcc libpq-dev \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY requirements.txt .

# RUN uv venv /app/venv && . /app/venv/bin/activate && uv pip sync --compile-bytecode requirements.txt
RUN uv venv venv && . venv/bin/activate && uv pip sync --compile-bytecode requirements.txt

# RUN uv venv venv && . venv/bin/activate && uv pip sync requirements.txt
COPY /backend .

FROM python:3.12-slim-bookworm

RUN apt-get update \
    && apt-get install -y --no-install-recommends nginx \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

COPY nginx/nginx.conf /etc/nginx/nginx.conf

COPY --from=builder /app /app
# COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/
WORKDIR /app

COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

EXPOSE 8000 80

ENTRYPOINT ["/entrypoint.sh"]

