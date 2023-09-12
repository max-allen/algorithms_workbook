import pytest


@pytest.fixture
def non_overlapping_ranges():
    return [[2, 4], [4, 6]]


@pytest.fixture
def sorted_intervals():
    return [
        {
            "existing_intervals": [[1, 3], [6, 9]],
            "insert_interval": [2, 5],
            "expected": [[1, 5], [6, 9]],
        },
        {
            "existing_intervals": [[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]],
            "insert_interval": [4, 8],
            "expected": [[1, 2], [3, 10], [12, 16]],
        },
    ]
