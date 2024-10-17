import pytest
from index import Queue

def test_queue_initialization():
    q = Queue()
    assert q.is_empty() is True
    assert q.size() == 0

def test_queue_enqueue():
    q = Queue()
    q.enqueue(10)
    assert q.is_empty() is False
    assert q.size() == 1
    assert q.peek() == 10

def test_queue_dequeue():
    q = Queue()
    q.enqueue(20)
    q.enqueue(30)
    assert q.dequeue() == 20
    assert q.size() == 1
    assert q.peek() == 30

def test_queue_peek():
    q = Queue()
    q.enqueue(40)
    assert q.peek() == 40
    assert q.size() == 1

def test_queue_dequeue_empty():
    q = Queue()
    with pytest.raises(IndexError, match="Dequeue from an empty queue"):
        q.dequeue()

def test_queue_peek_empty():
    q = Queue()
    with pytest.raises(IndexError, match="Peek from an empty queue"):
        q.peek()

def test_queue_clear():
    q = Queue()
    q.enqueue(20)
    q.enqueue(30)
    q.clear()
    assert q.is_empty() is True
    assert q.size() == 0
    
