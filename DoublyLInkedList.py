class Node:
    def __init__(self, data=None, prev=None, next=None):
        self.data = data
        self.prev = prev
        self.next = next

    def __repr__(self) -> str:
        return repr(self.data)
    
class DoublyLinkedList:
    def __init__(self):
        self.head = Node() # self node is Null node those have not data and prev and next have not node

    def __repr__(self) -> str:
        nodes = []
        current_node = self.head.next

        while current_node:
            nodes.append(repr(current_node))
            current_node = current_node.next

        return ",".join(nodes)

    #add node to the end of the node
    def append(self, data):
        node = Node(data) 

        if self.head.next is None:
            self.head.next = node
            return
        current_node = self.head.next
        while current_node.next:
            current_node = current_node.next

        current_node.next = node
        node.prev = current_node

    #add node start of the node 
    def prepend(self, data):
         first_node = self.head.next

         new_node = Node(data, None, first_node)
         self.head.next = new_node

         if first_node:
             first_node.prev = new_node

    #search the node item and return the item
    def search(self, item):
        current_node = self.head.next
        
        while current_node:
            if current_node.data == item:
                return current_node
            current_node = current_node.next

        return None

    def remove_node(self, node):
        if node.prev:
            node.prev.next = node.next
        else:
            self.head.next = node.next
        
        if node.next:
            node.next.prev = node.prev

    def remove(self, item):
        node = self.search(item)
        
        if node is None:
            return

        self.remove_node(node)

if __name__ == '__main__':
    dll = DoublyLinkedList()
    dll.append(10)
    dll.append(15)
    dll.append(20)
    dll.append(25)
    print(dll)
    dll.prepend(5)
    print(dll)
    print(dll.search(25))
    print(dll.search(55))
    dll.remove(10)
    print(dll)






    
