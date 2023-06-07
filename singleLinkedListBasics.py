class Node:
    def __init__(self,data) -> None:
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self) -> None:
        self.head = None
    def is_empty(self):
        return self.head is None
    def insert_at_head(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.head = new_node
        else:
            new_node.next = self.head
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
    def delete_at_head(self):
        if self.is_empty():
            print("LinkedList is empty.")
        self.head = self.head.next
    def delete_by_value(self,value):
        if self.is_empty():
            print("LinkedList is empty.")
            return
        if self.head.data == value:
            self.head = self.head.next
            return
        current = self.head
        prev = None
        while current and current.data != value:
            prev = current
            current = current.next
        if current is None:
            print("Given value is not found.")
            return
        prev.next = current.next

    def search(self,value):
        if self.is_empty():
            print("LinkedList is empty.")
            return False
        current = self.head
        while current:
            if current.data == value:
                return True
            current = current.next
        return False
    
    def display(self):
        if self.is_empty():
            print("LinkedList is empty.")
            return
        current = self.head
        while current:
            print(current.data, end = "->")
            current = current.next
        print("None")
        

# Now testing :

my_list = LinkedList()

my_list.insert_at_head(3)
my_list.insert_at_head(2)
my_list.insert_at_head(1)
my_list.insert_at_tail(4)

my_list.display()

my_list.delete_at_head()

print(my_list.search(3))  # Output: True
print(my_list.search(5))  # Output: False

my_list.display()  # Output: 2 -> 3 -> 4 -> None

'''
Extra Notes:


Linked List Basics:

- Linked list is a data structure consisting of nodes, where each node contains data and a reference to the next node.
- The first node is called the head of the linked list.
- Nodes are connected in a sequential manner, with the last node pointing to None/null.
- We can traverse the linked list by starting from the head and following the next references until reaching the end.

Node Class:
- A Node class represents an individual node in the linked list.
- Each node contains data and a next reference.
- The data attribute stores the value of the node.
- The next attribute points to the next node in the linked list.

Linked List Class:
- The LinkedList class manages the overall linked list.
- It has an instance variable head that points to the first node (head) of the linked list.
- It provides various methods to perform operations on the linked list.

Insertion in a Linked List:
- We can insert a new node at the head or the tail of the linked list.
- Inserting at the head involves creating a new node and updating the head reference.
- Inserting at the tail requires traversing the linked list to find the last node and updating its next reference.

Deletion in a Linked List:
- We can delete a node from the linked list based on its value.
- If the node to be deleted is the head, we update the head reference to point to the next node.
- Otherwise, we traverse the linked list to find the node to be deleted and update the next reference of the previous node.

Searching in a Linked List:
- We can search for a specific value in the linked list.
- We traverse the linked list and check the data of each node.
- If a node with the given value is found, we return True; otherwise, we return False.

Displaying the Linked List:
- We can display the elements of the linked list.
- Starting from the head, we traverse the linked list and print the data of each node.
- We use an arrow symbol (->) to indicate the connection between nodes.
'''