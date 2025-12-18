"""Shared test fixtures."""

import pytest
from fastapi.testclient import TestClient

from app.main import app
from app.models.item import ItemCreate


@pytest.fixture
def client():
    """FastAPI test client."""
    return TestClient(app)


@pytest.fixture
def sample_item():
    """Sample item for testing."""
    return ItemCreate(name="Sample Item", slug="sample-item", description="A sample item for testing")


@pytest.fixture
def sample_item_data():
    """Sample item as dict for API calls."""
    return {
        "name": "Sample Item",
        "slug": "sample-item",
        "description": "A sample item for testing",
    }
