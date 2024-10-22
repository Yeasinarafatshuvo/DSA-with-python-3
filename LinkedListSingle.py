class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

    
    def __repr__(self) -> str:
        return repr(self.data)


class LinkedList:
    def __init__(self):
        self.head = Node()

    def __repr__(self) -> str:
        nodes = []
        current_node = self.head.next

        while current_node:
            nodes.append(repr(current_node))
            current_node = current_node.next
        return ",".join(nodes)
    
    #add data start of the linked list
    def prepend(self, data): 
        node = Node(data, self.head.next)
        self.head.next = node

    #add data end of the list
    def append(self, data):
        node = Node(data)

        if self.head.next is None:
            self.head.next = node
            return
        current_node = self.head.next

        while current_node.next:
            current_node = current_node.next
        current_node.next = node

    #search item in node
    def search(self, item):
        current_node = self.head.next

        while current_node:
            if current_node.data == item:
                return current_node
            current_node = current_node.next
        return None
    
    #remove item from the list
    def remove(self, item):
        previous_node = self.head
        current_node = previous_node.next

        while current_node:
            if current_node.data == item:
                break
            previous_node = current_node
            current_node = current_node.next

        if current_node is None:
            return None
        
        if self.head == previous_node:
            self.head.next = current_node.next
        else:
            previous_node.next = current_node.next

    #add data any in linked list after any of node
    def insert(self, data, new_data):
        current_node = self.head.next

        while current_node:
            if current_node.data == data:
                new_node = Node(new_data, current_node.next)
                current_node.next = new_node
                break
            current_node = current_node.next


li = LinkedList()
#add item on end of the linked list
li.append(5)
li.append(10)
#add item on start or head of the  linked list 
li.prepend(1)
print(li)
#search node item 5
print(li.search(5))
#insert data after node 10
li.insert(10,20)
print(li)
#remove item form the linked list
li.remove(5)
print(li)
