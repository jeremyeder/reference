"""Pydantic models for Item resource."""

from datetime import datetime

from pydantic import BaseModel, Field, field_validator

from app.core.security import sanitize_string, validate_slug


class ItemBase(BaseModel):
    """Base model with shared fields."""

    name: str = Field(..., min_length=1, max_length=200)
    slug: str = Field(..., min_length=1, max_length=100)
    description: str | None = Field(None, max_length=1000)

    @field_validator("name")
    @classmethod
    def sanitize_name(cls, v: str) -> str:
        """Sanitize name field."""
        return sanitize_string(v, max_length=200)

    @field_validator("slug")
    @classmethod
    def validate_slug_field(cls, v: str) -> str:
        """Validate slug field."""
        return validate_slug(v)

    @field_validator("description")
    @classmethod
    def sanitize_description(cls, v: str | None) -> str | None:
        """Sanitize description field."""
        if v is None:
            return None
        return sanitize_string(v, max_length=1000)


class ItemCreate(ItemBase):
    """Model for creating an item."""

    pass


class ItemUpdate(BaseModel):
    """Model for updating an item."""

    name: str | None = Field(None, min_length=1, max_length=200)
    description: str | None = Field(None, max_length=1000)

    @field_validator("name")
    @classmethod
    def sanitize_name(cls, v: str | None) -> str | None:
        """Sanitize name field."""
        if v is None:
            return None
        return sanitize_string(v, max_length=200)

    @field_validator("description")
    @classmethod
    def sanitize_description(cls, v: str | None) -> str | None:
        """Sanitize description field."""
        if v is None:
            return None
        return sanitize_string(v, max_length=1000)


class Item(ItemBase):
    """Complete item model with all fields."""

    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        """Pydantic configuration."""

        from_attributes = True
