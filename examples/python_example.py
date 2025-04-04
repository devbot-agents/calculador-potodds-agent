#!/usr/bin/env python3
# Exemplo de como chamar o endpoint do agente usando Python

import requests
import json

url = "http://localhost:8000/api/v1/execute"
data = {
    "type": "exemplo_type",
    "properties": {
        "pot_size": {
            "type": 42
        },
        "call_amount": {
            "type": 42
        },
        "current_bet": {
            "type": 42
        },
        "hand_equity": {
            "type": 42,
            "description": "exemplo_description"
        }
    }
}

response = requests.post(url, json=data)
print("Status Code:", response.status_code)
print("Response:")
print(json.dumps(response.json(), indent=2))
