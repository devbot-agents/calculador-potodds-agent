from fastapi import FastAPI
from app.controllers.agent_controller import router as agent_router
import os

# Criar a aplicação FastAPI
app = FastAPI(
    title="calculador-potodds-agent",
    description="calcula potodds de uma mao de poker com base no valor do pot na forca da mao etc..",
    version="0.1.0",
)

# Incluir routers
app.include_router(agent_router)

# Health check endpoint
@app.get("/health")
async def health_check():
    """
    Endpoint para verificação de saúde da API.
    """
    return {"status": "healthy"} 