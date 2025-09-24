class Queue:
    
    def __init__(self):
        self.queue = []
    
    def enqueue(self, n):
        self.queue.append(n)
        return self.queue
    
    
    def dequeue(self):
        if not self.isEmpty():
            self.queue.pop(0)
            return self.queue
        else:
            return "Queue already empty"
    
    
    def isEmpty(self):
        return len(self.queue) == 0
    
    def peekItem(self):
        return self.queue[0]
    
    
q = Queue()
print(q.enqueue(2))
print(q.enqueue(3))
print(q.enqueue(4))
print(q.dequeue())
print(q.peekItem())