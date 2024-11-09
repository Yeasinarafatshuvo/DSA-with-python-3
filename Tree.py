class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def __repr__(self) -> str:
        return repr(self.data)
    
    def add_left(self, node):
        self.left = node
    
    def add_right(self, node):
        self.right = node
    
class BinaryTree:

    #create a Binary tree
    def create_tree(self):
        two = Node(2)
        seven = Node(7)
        nine = Node(9)
        two.add_left(seven)  # Pass Node object
        two.add_right(nine)  # Pass Node object
        one = Node(1)
        six = Node(6)
        seven.add_left(one)  # Pass Node object
        seven.add_right(six)  # Pass Node object
        five = Node(5)
        ten = Node(10)
        six.add_left(five)  # Pass Node object
        six.add_right(ten)  # Pass Node object
        eight = Node(8)
        nine.add_right(eight)  # Pass Node object
        three = Node(3)
        four = Node(4)
        eight.add_left(three)  # Pass Node object
        eight.add_right(four)  # Pass Node object

        return two
    
    #traverse the tree based on pre order algorithm --
    def pre_order(self, node):
        print(node)

        if node.left:
            self.pre_order(node.left)
        if node.right:
            self.pre_order(node.right)

    #traverse the tree based on post order algorithm
    def post_order(self, node):
        if node.left:
            self.post_order(node.left)
        if node.right:
            self.post_order(node.right)
        print(node)

    #traverse the tree based on In order algorithm
    def in_order(self, node):
        if node.left:
            self.in_order(node.left)
        print(node)
        if node.right:
            self.in_order(node.right)
        
    
if __name__ == '__main__':
    binary_tree = BinaryTree()
    root = binary_tree.create_tree()
    print('Pre Order Tree: ')
    binary_tree.pre_order(root)

    print('Post Order Tree: ')
    binary_tree.post_order(root)

    print('In Order Tree: ')
    binary_tree.in_order(root)
