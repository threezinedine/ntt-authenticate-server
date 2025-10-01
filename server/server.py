import logging
from typing import AsyncGenerator
from fastapi import FastAPI, Depends
from fastapi.responses import JSONResponse
from fastapi.logger import logger
from contextlib import asynccontextmanager
from models.user import User
from utils import Env
from services.database import GetDatabase, Database

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

    logger.info("Setting up database schema...")
    Database.Setup()
    logger.info("Database schema setup complete.")

    logger.info("Loading environment variables...")
    Env.Load()
    logger.info("Environment variables loaded.")
    yield

    logger.info("Tearing down database schema...")
    Database.Teardown()
    logger.info("Database schema teardown complete.")

app = FastAPI(lifespan=lifespan)

@app.post("/register", 
          tags=["Authentication"], 
          summary="Register a new user", 
          description="Register a new user with the provided username and password.")
def register(request: LoginRequest, db: Database = Depends(GetDatabase)) -> JSONResponse:
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
    user = User(id="", username=request.username, passwordHash=request.password, createdAt=0)
    db.CreateUser(user)

    createdUser = db.GetUserByUsername(request.username)
    assert createdUser is not None, "User creation failed."

    print(createdUser)

    return JSONResponse(status_code=201, content={})


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(
        "server:app",
        host="localhost",
        port=8000,
        reload=True,
    )
