from fastapi import FastAPI
from app.api import agent_routes
from app.api import health_routes

app = FastAPI()
app.include_router(agent_routes.router, prefix="/api", tags=["chat"])
app.include_router(health_routes.router, prefix="/api", tags=["health"])


@app.get("/")
def read_root():
    return {"message": "Graham the Professional", "docs": "/docs"}
