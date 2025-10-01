from typing import Literal
from dotenv import load_dotenv


class Env:
    """
    Used for easy access to environment variables which are loaded from a .env file.
    """

    DEV_MODE: Literal["development", "production"] = "development"

    DATABASE_TYPE: Literal["in-memory", "sql"] = "in-memory"

    @staticmethod
    def Load() -> None:
        """
        Run once at the start of the application to load environment variables.
        """
        load_dotenv()