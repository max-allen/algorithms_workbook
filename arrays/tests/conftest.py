import pytest


@pytest.fixture
def two_number_sum_match():
    return {"arr": [3, 5, -4, 8, 11, 1, -1, 6], "target": 10}


@pytest.fixture
def two_number_sum_no_match():
    return {"arr": [1, 0, 8, 11, 5, -1, 6], "target": 100}


@pytest.fixture
def two_sum_match():
    return [{"arr": [2, 7, 11, 15], "target": 9}, {"arr": [3, 2, 4], "target": 6}]


@pytest.fixture
def three_number_sum_multiple():
    return {
        "arr": [12, 3, 1, 2, -6, 5, -8, 6],
        "target": 0,
        "expected": [[-8, 2, 6], [-8, 3, 5], [-6, 1, 5]],
    }


@pytest.fixture
def three_number_sum_single():
    return {
        "arr": [1, 2, 3],
        "target": 6,
        "expected": [[1, 2, 3]],
    }


@pytest.fixture
def three_number_sum_no_match(three_number_sum_multiple):
    return {"arr": three_number_sum_multiple["arr"], "target": 1000, "expected": []}


@pytest.fixture
def is_mountain_peak_lists():
    return [[1, 2, 3, 4, 3, 2, 1], [1, 2, 1, 4, 3, 2, 1], [1, 2, 3, 4, 3, 4, 1]]
