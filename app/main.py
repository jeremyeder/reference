"""FastAPI application entry point."""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api import health
from app.api.v1 import items
from app.core.config import settings
from app.core.logging import setup_logging

# Setup structured logging
setup_logging(debug=settings.debug)

# Create FastAPI application
app = FastAPI(
    title=settings.app_name,
    version=settings.app_version,
    description="Ambient Code Reference - AI-assisted development best practices",
    docs_url="/docs",
    redoc_url="/redoc",
)

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Health endpoints (no prefix)
app.include_router(health.router)

# API v1 endpoints
app.include_router(items.router, prefix=settings.api_v1_prefix)


@app.get("/")
def root() -> dict[str, str]:
    """Root endpoint."""
    return {
        "message": "Ambient Code Reference API",
        "version": settings.app_version,
        "docs": "/docs",
    }
