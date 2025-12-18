"""Security utilities for input validation and sanitization."""

import re


def sanitize_string(value: str, max_length: int = 200) -> str:
    """
    Sanitize a string by removing dangerous characters and trimming whitespace.

    Args:
        value: The string to sanitize
        max_length: Maximum allowed length

    Returns:
        Sanitized string
    """
    if not value:
        return ""

    # Remove leading/trailing whitespace
    sanitized = value.strip()

    # Remove control characters and other dangerous characters
    sanitized = re.sub(r"[\x00-\x1f\x7f-\x9f]", "", sanitized)

    # Trim to max length
    if len(sanitized) > max_length:
        sanitized = sanitized[:max_length]

    return sanitized


def validate_slug(value: str) -> str:
    """
    Validate that a slug is URL-safe.

    Args:
        value: The slug to validate

    Returns:
        Validated slug

    Raises:
        ValueError: If slug is invalid
    """
    if not value:
        raise ValueError("Slug cannot be empty")

    # Only allow lowercase letters, numbers, and hyphens
    if not re.match(r"^[a-z0-9-]+$", value):
        raise ValueError("Slug must contain only lowercase letters, numbers, and hyphens")

    # Cannot start or end with hyphen
    if value.startswith("-") or value.endswith("-"):
        raise ValueError("Slug cannot start or end with a hyphen")

    # Cannot have consecutive hyphens
    if "--" in value:
        raise ValueError("Slug cannot contain consecutive hyphens")

    return value
