#using pyetest write the test case for all possible methods
from LinkedListSingle import LinkedList

def testAppend():
    li = LinkedList()
    li.append(10)
    li.append(20)
    li.append(30)
    assert repr(li) == "10,20,30"

def testPrepend():
    li = LinkedList()
    li.append(10)
    li.append(20)
    li.prepend(5)
    assert repr(li) == "5,10,20"

def testInsert():
    li = LinkedList()
    li.append(10)
    li.append(20)
    li.append(30)
    result = li.search(20)
    assert result.data == 20

def testRemove():
    li = LinkedList()
    li.append(10)
    li.append(20)
    li.append(30)
    li.remove(20)
    assert repr(li) == "10,30"

def testRemoveHead():
    li = LinkedList()
    li.append(10)
    li.append(20)
    li.append(30)
    li.remove(10)
    assert repr(li) == "20,30"

def testRemoveNonExistentItem():
    li = LinkedList()
    li.append(10)
    li.append(20)
    li.append(30)
    result = li.remove(40) #removing non existent item
    assert result is None
    assert repr(li) == "10,20,30"
