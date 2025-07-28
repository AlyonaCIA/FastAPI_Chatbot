"""FastAPI Chatbot Application - Entry Point."""
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# Load environment variables FIRST
from dotenv import load_dotenv
load_dotenv()

from app.core.config import settings
from app.core.logging import setup_logging
from app.api.v1.routes import conversation, health


def create_app() -> FastAPI:
    """Create and configure FastAPI application."""
    
    # Setup logging
    setup_logging()
    
    # Create FastAPI app
    app = FastAPI(
        title=settings.APP_NAME,
        version=settings.APP_VERSION,
        debug=settings.DEBUG,
        docs_url="/docs",  # ← Forzar docs siempre
        redoc_url="/redoc",  # ← Forzar redoc siempre
    )
    
    # Add CORS middleware
    app.add_middleware(
        CORSMiddleware,
        allow_origins=settings.ALLOWED_ORIGINS,
        allow_methods=settings.ALLOWED_METHODS,
        allow_headers=settings.ALLOWED_HEADERS,
    )
    
    # Include routers
    app.include_router(
        conversation.router, 
        prefix=settings.API_V1_PREFIX
    )
    app.include_router(
        health.router, 
        prefix=settings.API_V1_PREFIX
    )
    
    # Root endpoint
    @app.get("/")
    async def root():
        return {
            "message": f"{settings.APP_NAME} is running!",
            "version": settings.APP_VERSION,
            "debug": settings.DEBUG,
            "docs": "/docs",
            "endpoints": [
                "GET /",
                "GET /docs", 
                "GET /api/v1/health",
                "POST /api/v1/conversations/start",
                "POST /api/v1/conversations/{session_id}/messages"
            ]
        }
    
    return app


# Create app instance
app = create_app()


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        "app.main:app",
        host=settings.HOST,
        port=settings.PORT,
        reload=True  # ← Forzar reload para development
    )
