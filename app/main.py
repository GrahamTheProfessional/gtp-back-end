from fastapi import FastAPI

from fastapi.middleware.cors import CORSMiddleware
from app.api import agent_routes
from app.api import health_routes

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # Frontend URL
    allow_credentials=True,
    allow_methods=["*"],  # Allow all HTTP methods (GET, POST, etc.)
    allow_headers=["*"],  # Allow all headers
)

app.include_router(agent_routes.router, prefix="/api", tags=["chat"])
app.include_router(health_routes.router, prefix="/api", tags=["health"])


@app.get("/")
def read_root():
    return {"message": "Graham the Professional", "docs": "/docs"}
