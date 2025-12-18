"""Unit tests for ItemService."""

import pytest

from app.models.item import ItemCreate, ItemUpdate
from app.services.item_service import ItemService


def test_create_item():
    """Test creating a new item."""
    # Arrange
    service = ItemService()
    data = ItemCreate(name="Test Item", slug="test-item")

    # Act
    result = service.create_item(data)

    # Assert
    assert result.id == 1
    assert result.name == "Test Item"
    assert result.slug == "test-item"
    assert result.description is None
    assert result.created_at is not None
    assert result.updated_at is not None


def test_create_item_with_description():
    """Test creating an item with description."""
    service = ItemService()
    data = ItemCreate(name="Test Item", slug="test-item", description="A test description")

    result = service.create_item(data)

    assert result.description == "A test description"


def test_create_duplicate_slug_raises_error():
    """Test that duplicate slugs raise ValueError."""
    service = ItemService()
    data = ItemCreate(name="Test Item", slug="test-item")
    service.create_item(data)

    # Attempting to create duplicate should raise ValueError
    with pytest.raises(ValueError, match="already exists"):
        service.create_item(data)


def test_get_item():
    """Test retrieving an item by ID."""
    service = ItemService()
    created = service.create_item(ItemCreate(name="Test", slug="test"))

    result = service.get_item(created.id)

    assert result is not None
    assert result.id == created.id
    assert result.name == created.name


def test_get_item_not_found():
    """Test getting non-existent item returns None."""
    service = ItemService()

    result = service.get_item(999)

    assert result is None


def test_get_item_by_slug():
    """Test retrieving an item by slug."""
    service = ItemService()
    service.create_item(ItemCreate(name="Test", slug="test-slug"))

    result = service.get_item_by_slug("test-slug")

    assert result is not None
    assert result.slug == "test-slug"


def test_get_item_by_slug_not_found():
    """Test getting non-existent slug returns None."""
    service = ItemService()

    result = service.get_item_by_slug("nonexistent")

    assert result is None


def test_list_items_empty():
    """Test listing items when none exist."""
    service = ItemService()

    result = service.list_items()

    assert result == []


def test_list_items():
    """Test listing items."""
    service = ItemService()
    service.create_item(ItemCreate(name="Item 1", slug="item-1"))
    service.create_item(ItemCreate(name="Item 2", slug="item-2"))
    service.create_item(ItemCreate(name="Item 3", slug="item-3"))

    result = service.list_items()

    assert len(result) == 3
    assert result[0].name == "Item 1"
    assert result[1].name == "Item 2"
    assert result[2].name == "Item 3"


def test_list_items_pagination():
    """Test pagination."""
    service = ItemService()
    for i in range(10):
        service.create_item(ItemCreate(name=f"Item {i}", slug=f"item-{i}"))

    # Get items 2-4 (skip 2, limit 3)
    result = service.list_items(skip=2, limit=3)

    assert len(result) == 3
    assert result[0].name == "Item 2"
    assert result[1].name == "Item 3"
    assert result[2].name == "Item 4"


def test_update_item():
    """Test updating an item."""
    service = ItemService()
    created = service.create_item(ItemCreate(name="Original", slug="original"))

    update_data = ItemUpdate(name="Updated")
    result = service.update_item(created.id, update_data)

    assert result is not None
    assert result.name == "Updated"
    assert result.slug == "original"  # Slug unchanged
    assert result.updated_at > result.created_at


def test_update_item_not_found():
    """Test updating non-existent item returns None."""
    service = ItemService()

    result = service.update_item(999, ItemUpdate(name="Updated"))

    assert result is None


def test_delete_item():
    """Test deleting an item."""
    service = ItemService()
    created = service.create_item(ItemCreate(name="Test", slug="test"))

    result = service.delete_item(created.id)

    assert result is True
    assert service.get_item(created.id) is None


def test_delete_item_not_found():
    """Test deleting non-existent item returns False."""
    service = ItemService()

    result = service.delete_item(999)

    assert result is False
