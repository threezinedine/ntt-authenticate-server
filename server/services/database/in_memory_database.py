from .database import Database

class InMemoryDatabase(Database):
    def __init__(self) -> None:
        super().__init__()

    def _ConnectImpl(self, url: str) -> None:
        pass

    def _DisconnectImpl(self) -> None:
        pass