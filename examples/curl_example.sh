#!/bin/bash
# Exemplo de como chamar o endpoint do agente usando curl

curl -X POST \
  http://localhost:8000/api/v1/execute \
  -H "Content-Type: application/json" \
  -d '{"type": "exemplo_type", "properties": {"pot_size": {"type": 42}, "call_amount": {"type": 42}, "current_bet": {"type": 42}, "hand_equity": {"type": 42, "description": "exemplo_description"}}}'
