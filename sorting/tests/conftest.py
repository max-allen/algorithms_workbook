import pytest


@pytest.fixture
def integer_lists():
    return {
        "unsorted": [10, 9, 7, 15, 11, 2, 5, 6],
        "sorted": [2, 5, 6, 7, 9, 10, 11, 15],
    }
