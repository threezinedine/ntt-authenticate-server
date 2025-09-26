from fastapi.testclient import TestClient
from server import app

class Utils:
    def __init__(self) -> None:
        self.client = TestClient(app)
