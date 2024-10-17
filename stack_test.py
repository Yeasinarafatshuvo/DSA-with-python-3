import pytest
from index import Stack

def test_stack_initialization():
    s = Stack()
    assert s.is_empty() is True
    assert s.size() == 0

def test_stack_push():
    s = Stack()
    s.push(10)
    assert s.is_empty() is False
    assert s.size() == 1
    assert s.peek() == 10

def test_stack_pop():
    s = Stack()
    s.push(20)
    s.push(30)
    assert s.pop() == 30
    assert s.size() == 1
    assert s.peek() == 20

def test_stack_peek():
    s = Stack()
    s.push(40)
    assert s.peek() == 40
    assert s.size() == 1

def test_stack_pop_empty():
    s = Stack()
    with pytest.raises(IndexError, match="Pop from an empty stack"):
        s.pop()

def test_stack_peek_empty():
    s = Stack()
    with pytest.raises(IndexError, match="Peek from an empty stack"):
        s.peek()

def test_stack_clear():
    s = Stack()
    s.push(20)
    s.push(30)
    s.clear()
    assert s.is_empty() is True
    assert s.size() == 0
    


