import pytest
from stacks import Stack


@pytest.fixture
def stack():
    s = Stack()

    s.push("foo")
    s.push("bar")
    s.push("baz")
    return s


@pytest.fixture
def parentheses_inputs():
    return [("()", True), ("()[]{}", True), ("(]", False), ("(){", False)]


@pytest.fixture
def parentheses_repeating_input():
    return "((({{{}}})))"
