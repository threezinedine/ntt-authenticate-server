from typing import Generator
import pytest 
from tests.utils import Utils

@pytest.fixture
def utils() -> Generator[Utils, None, None]:
    utils = Utils()
    try:
        yield utils
    finally:
        utils.Cleanup()