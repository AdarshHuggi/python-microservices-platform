from fastapi.testclient import TestClient
from backend_api.api import app

client = TestClient(app)

def test_create_and_fetch_customer():
    created = client.post("/customers", json={"name":"Ada Lovelace","email":"ada@example.test"})
    assert created.status_code == 201
    customer_id = created.json()["id"]
    fetched = client.get(f"/customers/{customer_id}")
    assert fetched.status_code == 200
    assert fetched.json()["email"] == "ada@example.test"

def test_missing_customer_returns_404():
    response = client.get("/customers/does-not-exist")
    assert response.status_code == 404
