from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager    
import uvicorn



@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup actions
    print("Starting up...")
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

    @app.get("/")
    async def read_root():
        return {"message": "Hello, World!"}

    return app

if __name__ == "__main__":
    app = create_app()
    uvicorn.run(app, host="0.0.0.0", port=8000)