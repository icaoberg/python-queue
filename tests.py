import pytest
from Queue import Queue

def test_empty():
    q = Queue()
    assert q.is_empty()
    assert q.size() == 0
    assert len(q) == 0

def test_push():
    q = Queue()
    for i in range(100):
        q.push(i)
        assert q.size() == i + 1

def test_pop_order():
    q = Queue()
    for i in range(5):
        q.push(i)
    for i in range(5):
        assert q.pop() == i

def test_peek():
    q = Queue()
    q.push(42)
    assert q.peek() == 42
    assert q.size() == 1

def test_pop_empty():
    q = Queue()
    with pytest.raises(IndexError):
        q.pop()

def test_peek_empty():
    q = Queue()
    with pytest.raises(IndexError):
        q.peek()

def test_repr():
    q = Queue()
    q.push(1)
    q.push(2)
    assert repr(q) == "Queue([1, 2])"
