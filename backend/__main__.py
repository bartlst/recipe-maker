from contextlib import asynccontextmanager

import uvicorn
from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from middleware.auth import supabase_auth_middleware


@asynccontextmanager
async def lifespan(app: FastAPI):
    print("Starting up...")
    _ = load_dotenv()
    from api import base_router

    app.include_router(base_router)
    yield
    # Shutdown actions
    print("Shutting down...")


def create_app() -> FastAPI:
    app = FastAPI(lifespan=lifespan)

    # Configure CORS middleware
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],  # Adjust as needed for security
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    app.middleware("http")(supabase_auth_middleware)

    @app.get("/")
    async def read_root():
        return {"message": "Hello, World!"}

    return app


if __name__ == "__main__":
    app = create_app()
    uvicorn.run(app, host="0.0.0.0", port=8080)
