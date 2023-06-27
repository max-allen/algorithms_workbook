import pytest


@pytest.fixture
def key_count_fixture():
    return {
        "foo": {"bar": {}},
        "baz": {
            "quux": {"corge": {"foo": {"corge": {}}}},
        },
        "quux": {},
        "corge": {},
    }


@pytest.fixture
def two_number_sum_match():
    return {"arr": [3, 5, -4, 8, 11, 1, -1, 6], "target": 10}


@pytest.fixture
def two_number_sum_no_match():
    return {"arr": [1, 0, 8, 11, 5, -1, 6], "target": 100}


@pytest.fixture
def is_subsequence_valid():
    return {"arr": [5, 1, 22, 25, 6, -1, 8, 10], "sequence": [1, 6, -1, 10]}


@pytest.fixture
def is_subsequence_invalid_duplicate():
    return {"arr": [5, 1, 22, 25, 6, -1, 8, 10], "sequence": [1, 6, -1, -1]}


@pytest.fixture
def is_subsequence_invalid_non_members():
    return {
        "arr": [5, 1, 22, 25, 6, -1, 8, 10],
        "sequence": [1, 6, -1, 10, 11, 11, 11, 11],
    }
