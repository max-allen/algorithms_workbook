import pytest


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


@pytest.fixture
def is_palindrome_valid():
    return "abcdcba"


@pytest.fixture
def is_palindrome_invalid():
    return "abcdefg"


@pytest.fixture
def is_palindrome_valid_spaces():
    return "Was it a car or a cat I saw"
