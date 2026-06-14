```python
"""
DocuVerse FastAPI Application Entry Point
"""

from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
import os

from app.config import get_settings
from app.api.routes import router as api_router
from app.services.vector_store import VectorStoreService
from app.services.parser import ParserService
from app.utils import initialize_services, configure_cors

@asynccontextmanager
async def lifespan(app: FastAPI):
    """Application lifecycle management"""
    settings = get_settings()
    
    # Initialize services on startup
    initialize_services(app)
    
    yield
    
    # Cleanup on shutdown
    print("🛑 Shutting down DocuVerse services...")


def create_app() -> FastAPI:
    """Factory function to create FastAPI application"""
    settings = get_settings()
    
    app = FastAPI(
        title="DocuVerse API",
        description="Generative Media Documentation Engine - Transform codebases into interactive walkthroughs",
        version="1.0.0",
        docs_url="/api/docs",
        redoc_url="/api/redoc",
        openapi_url="/api/openapi.json",
        lifespan=lifespan,
    )
    
    # CORS Configuration - Allow frontend to make requests
    configure_cors(app, settings)
    
    # Include API routes
    app.include_router(api_router, prefix="/api")
    
    @app.get("/")
    async def root():
        """Root endpoint with API information"""
        return {
            "service": "DocuVerse API",
            "version": "1.0.0",
            "status": "running",
            "docs": "/api/docs",
            "redoc": "/api/redoc",
            "health": "/health"
        }
    
    @app.get("/health")
    async def health_check():
        """Health check endpoint"""
        return {
            "status": "healthy",
            "service": "DocuVerse API",
            "version": "1.0.0"
        }
    
    return app


app = create_app()


if __name__ == "__main__":
    import uvicorn
    settings = get_settings()
    uvicorn.run(
        "app.main:app",
        host=settings.host,
        port=settings.port,
        reload=settings.debug
    )
```

```python
# File: backend/app/utils.py

from app.services.vector_store import VectorStoreService
from app.services.parser import ParserService

def initialize_services(app):
    print("🚀 Initializing DocuVerse services...")
    
    # Initialize Vector Store
    vector_store = VectorStoreService()
    app.state.vector_store = vector_store
    
    # Initialize Parser Service
    parser_service = ParserService()
    app.state.parser = parser_service
    
    print("✅ DocuVerse services initialized successfully!")

def configure_cors(app, settings):
    allowed_origins = [
        "http://localhost:3000",
        "http://127.0.0.1:3000",
        settings.frontend_url,
    ]
    extra_origins = os.getenv("EXTRA_CORS_ORIGINS", "")
    if extra_origins:
        allowed_origins.extend([o.strip() for o in extra_origins.split(",") if o.strip()])

    origin_regex = r"https://(.*\.netlify\.app|.*\.awsapprunner\.com|logorhythms\.in)"

    app.add_middleware(
        CORSMiddleware,
        allow_origins=[o for o in allowed_origins if o],
        allow_origin_regex=origin_regex,
        allow_credentials=True,
        allow_methods=["GET", "POST", "PUT", "DELETE", "OPTIONS", "PATCH"],
        allow_headers=["*"],
        expose_headers=["*"],
    )
```