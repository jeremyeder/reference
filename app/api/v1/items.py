"""API endpoints for Item resource."""

from fastapi import APIRouter, HTTPException, status

from app.models.item import Item, ItemCreate, ItemUpdate
from app.services.item_service import item_service

router = APIRouter(prefix="/items", tags=["items"])


@router.post("/", response_model=Item, status_code=status.HTTP_201_CREATED)
def create_item(data: ItemCreate) -> Item:
    """
    Create a new item.

    Args:
        data: Item creation data

    Returns:
        Created item

    Raises:
        HTTPException: If slug already exists
    """
    try:
        return item_service.create_item(data)
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=str(e))


@router.get("/", response_model=list[Item])
def list_items(skip: int = 0, limit: int = 100) -> list[Item]:
    """
    List items with pagination.

    Args:
        skip: Number of items to skip
        limit: Maximum number of items to return

    Returns:
        List of items
    """
    return item_service.list_items(skip=skip, limit=limit)


@router.get("/{item_id}", response_model=Item)
def get_item(item_id: int) -> Item:
    """
    Get item by ID.

    Args:
        item_id: Item ID

    Returns:
        Item

    Raises:
        HTTPException: If item not found
    """
    item = item_service.get_item(item_id)
    if item is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Item not found")
    return item


@router.get("/slug/{slug}", response_model=Item)
def get_item_by_slug(slug: str) -> Item:
    """
    Get item by slug.

    Args:
        slug: Item slug

    Returns:
        Item

    Raises:
        HTTPException: If item not found
    """
    item = item_service.get_item_by_slug(slug)
    if item is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Item not found")
    return item


@router.patch("/{item_id}", response_model=Item)
def update_item(item_id: int, data: ItemUpdate) -> Item:
    """
    Update an existing item.

    Args:
        item_id: Item ID
        data: Update data

    Returns:
        Updated item

    Raises:
        HTTPException: If item not found
    """
    item = item_service.update_item(item_id, data)
    if item is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Item not found")
    return item


@router.delete("/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_item(item_id: int) -> None:
    """
    Delete an item.

    Args:
        item_id: Item ID

    Raises:
        HTTPException: If item not found
    """
    if not item_service.delete_item(item_id):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Item not found")
