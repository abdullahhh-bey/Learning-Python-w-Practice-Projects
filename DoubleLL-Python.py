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
        
        
    def insert_beginning(self , data):
        node = Node(data)
        temp = self.head 
        if temp == None:
            self.head = node
        
        node.next = temp
        temp.prev = node 
        self.head = node 
        
    
    
        
        
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
        
        print("\n")
    
    
    
    def removeItem(self,key):
        temp = self.head
        if self.IsEmpty():
            print("Empty")
            return
        if temp.data == key:
            self.head = temp.next
            self.head.prev = None
            return

        previous = temp
        while temp.next:
            temp = temp.next
            if temp.data == key:
                previous.next = temp.next
                temp.next.prev = previous
                print("Deleted")
                return
            previous = temp
            
        print("Not Found")
        
        
        
dl = DoubleLL()
dl.displayItems()
dl.insertRear(1)
dl.insertRear(2)
dl.insertRear(1)
dl.displayItems()
dl.insert_beginning(10)
dl.displayItems()
dl.removeItem(1)
dl.removeItem(11)
dl.displayItems()
