import pytest  # type: ignore
from .utils import Utils


def test_register(utils: Utils):
    response = utils.client.post("/register", json={"username": "test", "password": "test"})
    assert response.status_code == 201
