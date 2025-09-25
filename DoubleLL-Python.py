class Node: 
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None
        

class DoubleLL:
    def __init__(self):
        self.head = None
      
        
    def insertRear(self , data):
        temp = self.head 
        node = Node(data)
        
        if not temp:
            self.head = node
            return
        
        if temp.next == None:
            temp.next = node
            node.prev = temp
            return

        while temp.next:
            temp = temp.next
        temp.next = node 
        node.prev = temp
        
        
    def IsEmpty(self):
        return self.head == None
       
        
    def displayItems(self):
        temp = self.head
        if self.IsEmpty():
            print("Empty List!")
            return
        
        while temp:
            print(temp.data , end=" ")
            temp = temp.next
        
dl = DoubleLL()
dl.displayItems()
dl.insertRear(1)
dl.insertRear(2)
dl.insertRear(1)
dl.displayItems()
