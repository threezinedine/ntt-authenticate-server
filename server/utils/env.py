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

    @staticmethod
    def GetURL() -> str:
        """
        Get the database URL from environment variables.

        Returns
        -------
        str
            The database URL.
        """

        if Env.DATABASE_TYPE == "in-memory":
            return "in-memory://"
        elif Env.DATABASE_TYPE == "sql":
            raise NotImplementedError("SQL Database not implemented yet.")
        else:
            raise ValueError(f"Unsupported database type: {Env.DATABASE_TYPE}")