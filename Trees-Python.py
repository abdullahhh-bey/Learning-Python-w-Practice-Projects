class Node:
    def __init__(self , data):
        self.data = data
        self.left = None
        self.right = None
        
class BST:
    def __init__(self):
        self.root = None
    
    def insertItem(self , data):
        node = Node(data)
        if self.root is None:
            self.root = node
        
        found = True
        temp = self.root
        while found:
            if temp.data > data:
                if temp.left is None:
                    temp.left = node
                    return
                else:
                    temp = temp.left
            else:
                if temp.right is None:
                    temp.right = node
                    return
                else:
                    temp = temp.right
        
    def inOrder(self, node):
        if node is None:
            return
        self.inOrder(node.left)
        print(node.data , " ")
        self.inOrder(node.right)
        
        
tree = BST()
for v in range(1,5):
    tree.insertItem(v)
    
tree.inOrder()