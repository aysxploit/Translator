# syntax=docker/dockerfile:1.7
# Python 3.13, multi-stage targets for backend (FastAPI) and UI (Gradio).

ARG PYTHON_VERSION=3.13-slim

############################
# Base image
############################
FROM python:${PYTHON_VERSION} AS base
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1 \
    PIP_DISABLE_PIP_VERSION_CHECK=1
WORKDIR /app

# System deps (add build-essential only if you compile wheels)
RUN apt-get update -y && \
    apt-get install -y --no-install-recommends \
      curl ca-certificates && \
    rm -rf /var/lib/apt/lists/*

# Install Python deps
COPY requirements.txt .
RUN python -m pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# App sources
COPY main.py app.py ./
COPY .env.example ./.env.example

# Non-root user
RUN useradd --create-home --uid 10001 appuser && chown -R appuser:appuser /app
USER appuser

############################
# Backend target (FastAPI)
############################
FROM base AS backend
EXPOSE 8000
ENV UVICORN_HOST=0.0.0.0 \
    UVICORN_PORT=8000 \
    UVICORN_WORKERS=1
# Healthcheck for container orchestrators
HEALTHCHECK --interval=30s --timeout=5s --retries=3 \
  CMD curl -fsS "http://127.0.0.1:${UVICORN_PORT}/health" || exit 1
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]

############################
# UI target (Gradio)
############################
FROM base AS ui
EXPOSE 7860
# API_BASE_URL should point to the backend (e.g., http://backend:8000 in Compose)
ENV API_BASE_URL=http://localhost:8000 \
    TIMEOUT_SECONDS=15
CMD ["python", "app.py"]