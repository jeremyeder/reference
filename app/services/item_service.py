"""Service layer for Item resource business logic."""

from datetime import datetime

from app.models.item import Item, ItemCreate, ItemUpdate


class ItemService:
    """Service for managing items with in-memory storage."""

    def __init__(self) -> None:
        """Initialize service with empty storage."""
        self._items: dict[int, Item] = {}
        self._next_id: int = 1
        self._slug_index: dict[str, int] = {}

    def create_item(self, data: ItemCreate) -> Item:
        """
        Create a new item.

        Args:
            data: Item creation data

        Returns:
            Created item

        Raises:
            ValueError: If slug already exists
        """
        if data.slug in self._slug_index:
            raise ValueError(f"Item with slug '{data.slug}' already exists")

        now = datetime.utcnow()
        item = Item(
            id=self._next_id,
            name=data.name,
            slug=data.slug,
            description=data.description,
            created_at=now,
            updated_at=now,
        )

        self._items[item.id] = item
        self._slug_index[item.slug] = item.id
        self._next_id += 1

        return item

    def get_item(self, item_id: int) -> Item | None:
        """
        Get item by ID.

        Args:
            item_id: Item ID

        Returns:
            Item if found, None otherwise
        """
        return self._items.get(item_id)

    def get_item_by_slug(self, slug: str) -> Item | None:
        """
        Get item by slug.

        Args:
            slug: Item slug

        Returns:
            Item if found, None otherwise
        """
        item_id = self._slug_index.get(slug)
        if item_id is None:
            return None
        return self._items.get(item_id)

    def list_items(self, skip: int = 0, limit: int = 100) -> list[Item]:
        """
        List items with pagination.

        Args:
            skip: Number of items to skip
            limit: Maximum number of items to return

        Returns:
            List of items
        """
        all_items = sorted(self._items.values(), key=lambda x: x.id)
        return all_items[skip : skip + limit]

    def update_item(self, item_id: int, data: ItemUpdate) -> Item | None:
        """
        Update an existing item.

        Args:
            item_id: Item ID
            data: Update data

        Returns:
            Updated item if found, None otherwise
        """
        item = self._items.get(item_id)
        if item is None:
            return None

        update_data = data.model_dump(exclude_unset=True)
        for field, value in update_data.items():
            setattr(item, field, value)

        item.updated_at = datetime.utcnow()
        return item

    def delete_item(self, item_id: int) -> bool:
        """
        Delete an item.

        Args:
            item_id: Item ID

        Returns:
            True if deleted, False if not found
        """
        item = self._items.get(item_id)
        if item is None:
            return False

        del self._items[item_id]
        del self._slug_index[item.slug]
        return True


# Singleton instance
item_service = ItemService()
