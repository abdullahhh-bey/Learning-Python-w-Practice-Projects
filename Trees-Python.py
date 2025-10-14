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
        
        temp = self.root
        while True:
            if temp.data > data:
                if temp.left is None:
                    temp.left = node
                    break
                else:
                    temp = temp.left
            elif temp.data < data:
                if temp.right is None:
                    temp.right = node
                    break
                else:
                    temp = temp.right
            else:
                print("No Duplicates")
                break
            
        
    def inOrder(self, node):
        if node is None:
            return
        self.inOrder(node.left)
        print(node.data , " ")
        self.inOrder(node.right)
        
        
tree = BST()
tree.insertItem(5)
tree.insertItem(3)
tree.insertItem(19)
tree.insertItem(7)
tree.insertItem(1)
tree.insertItem(20)
    
tree.inOrder(tree.root)