FROM python:3.13-slim

COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

ARG SECRET_KEY
ARG SECRET_KEY_VALUE

ENV SecretKey=${SECRET_KEY}
ENV SecretKeyValue=${SECRET_KEY_VALUE}

WORKDIR /app
COPY . /app
RUN uv sync --frozen --no-cache

CMD ["/app/.venv/bin/fastapi", "run", "main.py", "--port", "8000", "--host", "0.0.0.0"]