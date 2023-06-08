class Queue:
    def __init__(self) -> None:
        self.queue = []
    
    def enqueue(self,data):
        self.queue.append(data)
    def dequeue(self):
        if not self.is_empty():
            return self.queue.pop(0)
        else:
            print("Queue is Empty!")
    def front(self):
        if not self.is_empty():
            return self.queue[0]
        else:
            print("Queue is Empty!")
    def is_empty(self):
        return len(self.queue) == 0
    def size(self):
        return len(self.queue)
    
# Now Testing :

queue = Queue()

queue.enqueue(10)
queue.enqueue(20)
queue.enqueue(30)

print(queue.front())  # Output: 10

queue.dequeue()
queue.dequeue()

print(queue.size())  # Output: 1
print(queue.queue[0]) # Output: 30