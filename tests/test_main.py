import pytest
from fastapi.testclient import TestClient
from jsonschema import validate

from main import app  # Assumindo que o FastAPI app está definido em main.py

client = TestClient(app)

output_schema = {
    "type": "object",
    "properties": {
        "pot_odds_percent": {"type": "string"},
        "is_call_profitable": {"type": "string"},
        "break_even_equity": {"type": "string"}
    },
    "required": ["pot_odds_percent", "is_call_profitable", "break_even_equity"]
}

@pytest.fixture
def example_input():
    return {
        "pot_size": 100,
        "call_amount": 10,
        "current_bet": 10,
        "hand_equity": 0.5
    }

def test_health_endpoint():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}

def test_execute_endpoint(example_input):
    response = client.post("/api/v1/execute", json=example_input)
    assert response.status_code == 200
    data = response.json()
    validate(instance=data, schema=output_schema)
    assert data["pot_odds_percent"] is not None
    assert data["is_call_profitable"] in ["true", "false"]
    assert data["break_even_equity"] is not None
