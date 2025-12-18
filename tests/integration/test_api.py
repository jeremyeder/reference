"""Integration tests for API endpoints."""


def test_health_check(client):
    """Test health check endpoint."""
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json() == {"status": "healthy"}


def test_readiness_check(client):
    """Test readiness probe endpoint."""
    response = client.get("/readiness")

    assert response.status_code == 200
    assert response.json() == {"status": "ready"}


def test_liveness_check(client):
    """Test liveness probe endpoint."""
    response = client.get("/liveness")

    assert response.status_code == 200
    assert response.json() == {"status": "alive"}


def test_root_endpoint(client):
    """Test root endpoint."""
    response = client.get("/")

    assert response.status_code == 200
    data = response.json()
    assert "message" in data
    assert "version" in data
    assert data["docs"] == "/docs"


def test_create_item(client, sample_item_data):
    """Test creating an item."""
    response = client.post("/api/v1/items", json=sample_item_data)

    assert response.status_code == 201
    data = response.json()
    assert data["name"] == sample_item_data["name"]
    assert data["slug"] == sample_item_data["slug"]
    assert data["description"] == sample_item_data["description"]
    assert "id" in data
    assert "created_at" in data
    assert "updated_at" in data


def test_create_item_duplicate_slug(client, sample_item_data):
    """Test creating item with duplicate slug returns 409."""
    # Create first item
    client.post("/api/v1/items", json=sample_item_data)

    # Attempt duplicate
    response = client.post("/api/v1/items", json=sample_item_data)

    assert response.status_code == 409
    assert "already exists" in response.json()["detail"]


def test_create_item_invalid_slug(client):
    """Test creating item with invalid slug returns 422."""
    response = client.post("/api/v1/items", json={"name": "Test", "slug": "Invalid Slug!"})

    assert response.status_code == 422


def test_list_items_empty(client):
    """Test listing items when none exist."""
    response = client.get("/api/v1/items")

    assert response.status_code == 200
    assert response.json() == []


def test_list_items(client, sample_item_data):
    """Test listing items."""
    # Create items
    for i in range(3):
        data = sample_item_data.copy()
        data["slug"] = f"item-{i}"
        client.post("/api/v1/items", json=data)

    response = client.get("/api/v1/items")

    assert response.status_code == 200
    items = response.json()
    assert len(items) == 3


def test_list_items_pagination(client, sample_item_data):
    """Test pagination."""
    # Create 10 items
    for i in range(10):
        data = sample_item_data.copy()
        data["slug"] = f"item-{i}"
        client.post("/api/v1/items", json=data)

    response = client.get("/api/v1/items?skip=2&limit=3")

    assert response.status_code == 200
    items = response.json()
    assert len(items) == 3


def test_get_item(client, sample_item_data):
    """Test getting item by ID."""
    # Create item
    create_response = client.post("/api/v1/items", json=sample_item_data)
    item_id = create_response.json()["id"]

    response = client.get(f"/api/v1/items/{item_id}")

    assert response.status_code == 200
    data = response.json()
    assert data["id"] == item_id
    assert data["name"] == sample_item_data["name"]


def test_get_item_not_found(client):
    """Test getting non-existent item returns 404."""
    response = client.get("/api/v1/items/999")

    assert response.status_code == 404
    assert response.json()["detail"] == "Item not found"


def test_get_item_by_slug(client, sample_item_data):
    """Test getting item by slug."""
    # Create item
    client.post("/api/v1/items", json=sample_item_data)

    response = client.get(f"/api/v1/items/slug/{sample_item_data['slug']}")

    assert response.status_code == 200
    data = response.json()
    assert data["slug"] == sample_item_data["slug"]


def test_get_item_by_slug_not_found(client):
    """Test getting non-existent slug returns 404."""
    response = client.get("/api/v1/items/slug/nonexistent")

    assert response.status_code == 404


def test_update_item(client, sample_item_data):
    """Test updating an item."""
    # Create item
    create_response = client.post("/api/v1/items", json=sample_item_data)
    item_id = create_response.json()["id"]

    # Update
    response = client.patch(f"/api/v1/items/{item_id}", json={"name": "Updated Name"})

    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "Updated Name"
    assert data["slug"] == sample_item_data["slug"]  # Unchanged


def test_update_item_not_found(client):
    """Test updating non-existent item returns 404."""
    response = client.patch("/api/v1/items/999", json={"name": "Updated"})

    assert response.status_code == 404


def test_delete_item(client, sample_item_data):
    """Test deleting an item."""
    # Create item
    create_response = client.post("/api/v1/items", json=sample_item_data)
    item_id = create_response.json()["id"]

    # Delete
    response = client.delete(f"/api/v1/items/{item_id}")

    assert response.status_code == 204

    # Verify deleted
    get_response = client.get(f"/api/v1/items/{item_id}")
    assert get_response.status_code == 404


def test_delete_item_not_found(client):
    """Test deleting non-existent item returns 404."""
    response = client.delete("/api/v1/items/999")

    assert response.status_code == 404
