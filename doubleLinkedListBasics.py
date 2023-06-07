class Node:
    def __init__(self,data) -> None:
        self.data = data
        self.prev = None
        self.next = None

'''
Just need to remember while performing any operations on 
the DoublyLinkedList that we need to take care of 3 things, 
the data, the prev link and the next link
'''
class DoublyLinkedList:
    def __init__(self) -> None:
        self.head = None

    def is_empty(self):
        return self.head is None
    def insert_at_head(self,data):
        new_node = Node(data)
        if self.is_empty():
            self.head = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
    def insert_at_tail(self,data):
        new_node = Node(data)
        if self.is_empty():
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
            new_node.prev = current
    def delete_at_head(self):
        if self.is_empty():
            print("DoublyLinkedList is empty!")
        elif self.head.next is None:
            self.head is None
        else:
            self.head = self.head.next
            self.head.prev = None

    def delete_at_tail(self):
        if self.is_empty():
            print("DoublyLinkedList is empty!")
        elif self.head.next is None:
            self.head is None
        else:
            current = self.head
            while current.next:
                current = current.next
            current.prev.next = None
    def display_forward(self):
        if self.is_empty():
            print("DoublyLinkedList is empty!")
        else:
            current = self.head
            while(current):
                print(current.data, end="<->")
                current = current.next
            print("None")
    def display_backward(self):
        if self.is_empty():
            print("DoublyLinkedList is empty!")
        else:
            current = self.head
            while(current.next):
                current = current.next
            while current:
                print(current.data, end="<->")
                current = current.prev
            print("None")


# Now Testing :

# Create a new doubly linked list
dll = DoublyLinkedList()

# Test insert_at_head() method
dll.insert_at_head(10)
dll.insert_at_head(20)
dll.insert_at_head(30)

# Display the doubly linked list (forward and backward)
dll.display_forward()  # Output: 30 <-> 20 <-> 10 <-> None
dll.display_backward()  # Output: 10 <-> 20 <-> 30 <-> None

# Test insert_at_tail() method
dll.insert_at_tail(40)
dll.insert_at_tail(50)

# Display the doubly linked list (forward and backward)
dll.display_forward()  # Output: 30 <-> 20 <-> 10 <-> 40 <-> 50 <-> None
dll.display_backward()  # Output: 50 <-> 40 <-> 10 <-> 20 <-> 30 <-> None

# Test delete_at_head() method
dll.delete_at_head()

# Display the doubly linked list (forward and backward)
dll.display_forward()  # Output: 20 <-> 10 <-> 40 <-> 50 <-> None
dll.display_backward()  # Output: 50 <-> 40 <-> 10 <-> 20 <-> None

# Test delete_at_tail() method
dll.delete_at_tail()

# Display the doubly linked list (forward and backward)
dll.display_forward()  # Output: 20 <-> 10 <-> 40 <-> None
dll.display_backward()  # Output: 40 <-> 10 <-> 20 <-> None

            