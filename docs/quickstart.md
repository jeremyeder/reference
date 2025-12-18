# Quickstart Guide

Get the Ambient Code Reference Repository running in 5 minutes.

## Prerequisites

- Python 3.11 or 3.12
- `uv` (recommended) or `pip`
- Git

## Setup

### 1. Clone the Repository

```bash
git clone https://github.com/jeremyeder/reference.git
cd reference
```

### 2. Run Setup Script

```bash
./scripts/setup.sh
```

This script:
- Creates virtual environment
- Installs dependencies
- Verifies installation

### 3. Activate Virtual Environment

```bash
source .venv/bin/activate
```

### 4. Start the Application

```bash
uvicorn app.main:app --reload
```

The application starts at `http://localhost:8000`.

## First API Call

### Health Check

```bash
curl http://localhost:8000/health
```

Response:
```json
{"status": "healthy"}
```

### Create an Item

```bash
curl -X POST http://localhost:8000/api/v1/items \
  -H "Content-Type: application/json" \
  -d '{
    "name": "My First Item",
    "slug": "my-first-item",
    "description": "A test item"
  }'
```

Response:
```json
{
  "id": 1,
  "name": "My First Item",
  "slug": "my-first-item",
  "description": "A test item",
  "created_at": "2025-12-17T12:00:00",
  "updated_at": "2025-12-17T12:00:00"
}
```

### List Items

```bash
curl http://localhost:8000/api/v1/items
```

## Interactive API Documentation

Visit:
- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc

## Run Tests

```bash
pytest
```

## Run Linters

```bash
# Format code
black app/ tests/

# Sort imports
isort app/ tests/

# Lint
ruff check app/ tests/
```

## Next Steps

- **[Architecture](architecture.md)** - Understand the layered architecture
- **[Tutorial](tutorial.md)** - Build your first feature
- **[API Reference](api-reference.md)** - Complete API documentation

## Troubleshooting

**Virtual environment not activating?**
```bash
python3.11 -m venv .venv
source .venv/bin/activate
```

**Dependency installation failing?**
```bash
uv pip install -r requirements-dev.txt
```

**Port 8000 already in use?**
```bash
uvicorn app.main:app --reload --port 8001
```
