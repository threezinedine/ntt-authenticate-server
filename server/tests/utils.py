from fastapi.testclient import TestClient
from server import app
from services.database import InMemoryDatabase

class Utils:
    def __init__(self) -> None:
        database = InMemoryDatabase()
        database.Connect()

        database.Setup()

        self.client = TestClient(app)

    def Cleanup(self) -> None:
        """
        Complete remove the database schema. 
        """
        database = InMemoryDatabase()
        database.Teardown()
