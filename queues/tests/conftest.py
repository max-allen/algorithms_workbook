import pytest

from queues import Queue


@pytest.fixture
def queue():
    q = Queue()

    q.enqueue("foo")
    q.enqueue("bar")
    q.enqueue("baz")
    return q
