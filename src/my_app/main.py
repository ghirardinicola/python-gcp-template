"""FastAPI application entrypoint."""

from fastapi import FastAPI

app = FastAPI(
    title="My App",
    description="Python GCP Cloud Run Application",
    version="0.1.0",
)


@app.get("/health")
async def health() -> dict:
    """Health check endpoint."""
    return {"status": "healthy"}


@app.get("/")
async def root() -> dict:
    """Root endpoint."""
    return {"message": "Hello, World!"}
