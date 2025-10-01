from typing import Generator
from .database import *
from .in_memory_database import *
from utils.env import Env

def GetDatabase() -> Generator[Database, None, None]:
    if Env.DATABASE_TYPE == "sql":
        raise NotImplementedError("SQL Database not implemented yet.")
    elif Env.DATABASE_TYPE == "in-memory":
        db = InMemoryDatabase()
    else:
        raise ValueError(f"Unsupported database type: {Env.DATABASE_TYPE}")

    try:
        db.Connect()
        yield db
    finally:
        db.Disconnect()