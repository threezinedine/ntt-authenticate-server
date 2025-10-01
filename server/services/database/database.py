from abc import ABC, abstractmethod

from models.user import User
from utils import Env


class Database(ABC):
    def __init__(self) -> None:
        pass

    @staticmethod
    def Setup() -> None:
        """
        Setup the database schema.
        """
        if Env.DATABASE_TYPE == "in-memory":
            from .in_memory_database import InMemoryDatabase

            InMemoryDatabase.Setup()

    @staticmethod
    def Teardown() -> None:
        """
        Teardown the database schema.
        """
        if Env.DATABASE_TYPE == "in-memory":
            from .in_memory_database import InMemoryDatabase

            InMemoryDatabase.Teardown()

    def Connect(self) -> None:
        """
        Establish a connection to the database.  

        Parameters
        ----------
        url : str
            The database connection URL.
        """
        self._ConnectImpl()

    def Disconnect(self) -> None:
        """
        Close the connection to the database.
        """
        self._DisconnectImpl()

    @abstractmethod
    def _ConnectImpl(self) -> None:
        """
        Actual implementation of the Connect method.
        """
        raise NotImplementedError("Connect method not implemented.")

    @abstractmethod
    def _DisconnectImpl(self) -> None:
        """
        Actual implementation of the Disconnect method.
        """
        raise NotImplementedError("Disconnect method not implemented.")

    # ====================== CRUD Operations ======================
    @abstractmethod
    def CreateUser(self, user: User) -> None:
        """
        Create a new user in the database.

        Parameters
        ----------
        user : User
            The user to create.
        """
        raise NotImplementedError("CreateUser method not implemented.")

    @abstractmethod
    def GetUserByUsername(self, username: str) -> User | None:
        """
        Retrieve a user by their username.

        Parameters
        ----------
        username : str
            The username of the user to retrieve.

        Returns
        -------
        User | None
            The user if found, otherwise None.
        """
        raise NotImplementedError("GetUserByUsername method not implemented.")