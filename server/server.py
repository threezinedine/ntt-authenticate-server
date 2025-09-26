import logging
from typing import AsyncGenerator
from fastapi import FastAPI
from fastapi.logger import logger
from contextlib import asynccontextmanager
from utils import Env

from schemas import LoginRequest

@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncGenerator[None, None]:
    formatter = logging.Formatter(
        "[%(levelname)s] %(asctime)s - %(message)s", datefmt="%Y-%m-%d %H:%M:%S"
    )

    handler = logging.StreamHandler()
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    logger.setLevel(logging.INFO)

    logger.info("Loading environment variables...")
    Env.Load()
    yield

app = FastAPI(lifespan=lifespan)

@app.post("/register", tags=["Authentication"], summary="Register a new user", description="Register a new user with the provided username and password.")
def register(request: LoginRequest) -> None:
    """
    Register a new user.

    Parameters
    ----------
    request : LoginRequest
        The login request containing username and password.

    Returns
    -------
    RegisterResponse
        An empty response indicating successful registration.
    """
    logger.info(f"Registering user: {request.username}")
    # Here you would add logic to save the user to the database.
    return 


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(
        "server:app",
        host="localhost",
        port=8000,
        reload=True,
    )
