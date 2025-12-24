from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes import route_optimizer

app = FastAPI(
    title="Green Route Optimizer API",
    description="Dual-mode routing system for fuel and EV vehicles",
    version="1.0.0"
)

# CORS configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Update in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Register routers
app.include_router(route_optimizer.router)

@app.get("/")
async def root():
    return {
        "message": "Green Route Optimizer API",
        "docs": "/docs",
        "health": "/route/health"
    }