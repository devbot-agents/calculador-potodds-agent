from pydantic import BaseModel, Field
from typing import Dict, List, Any, Optional

# Modelo de entrada para o agente
class InputModel(BaseModel):
    # Este é um placeholder que será substituído 
    # pelos campos definidos no schema de entrada
    type: object
    properties: dict

# Modelo de saída para o agente
class OutputModel(BaseModel):
    # Este é um placeholder que será substituído 
    # pelos campos definidos no schema de saída
    type: object
    properties: dict 