class Node:
    def __init__(self , data):
        self.data = data
        self.next = None
        
class LinkedList:
    def __init__(self):
        self.head = None
        
    def display(self):
        #checking if LL is empty
        temp = self.head
        if not temp:
            print("Empty\n")
        
        while temp:
            print(temp.data , end=" -> ")
            temp = temp.next
       
        
    def insertRear(self, data):
        node = Node(data)
        temp = self.head
        while temp.next:
            temp = temp.next
        
        temp.next = node
        print("Inserted")
    
    
    
    
    def insertBeginning(self, data):
        node = Node(data)
        temp = self.head
        self.head = node
        node.next = temp
        print("Inserted")
        
        
        
    def removeItem(self, data):
        temp = self.head
        if not temp:
            print("Empty!")
        
        if temp.data == data:
            self.head = temp.next
            
        prev = self.head
        while temp:
            prev = temp
            temp = temp.next
            if temp.data == data and temp:
                prev.next = temp.next
                print("Removed")
                break
       
        
    def IsEmpty(self):
        return self.head == None
        
        
    def searchItem(self, key):
        if self.IsEmpty():
            print("\nList is Empty")
        
        temp = self.head 
        while temp:
            if temp.data == key:
                print("\nFound")
                return
            else: 
                temp = temp.next
        
        print("\nNot Found")
  
  

l = LinkedList()
l.insertBeginning(1)
l.insertRear(3)
l.insertBeginning(8) 
l.display()
l.removeItem(3)
l.display()
l.searchItem(1)
