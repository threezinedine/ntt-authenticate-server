from abc import ABC, abstractmethod


class Database(ABC):
    def __init__(self) -> None:
        pass

    def Connect(self, url: str) -> None:
        """
        Establish a connection to the database.  

        Parameters
        ----------
        url : str
            The database connection URL.
        """
        self._ConnectImpl(url)

    def Disconnect(self) -> None:
        """
        Close the connection to the database.
        """
        self._DisconnectImpl()

    @abstractmethod
    def _ConnectImpl(self, url: str) -> None:
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