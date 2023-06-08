class StackEmptyError(Exception):
    pass

class Stack:
    def __init__(self):
        self.stack = []
        
    def push(self, data):
        self.stack.append(data)
        
    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        else:
            raise StackEmptyError("The Stack is empty.")
            
    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
        else:
            raise StackEmptyError("The Stack is empty.")
            
    def is_empty(self):
        return len(self.stack) == 0
    
    def size(self):
        return len(self.stack)

# Usage example:
stack = Stack()
try:
    stack.pop()
except StackEmptyError as e:
    print(e)  # Output: The Stack is empty.

# Custom exception `StackEmptyError` is used to represent an empty stack error.
# It is raised when attempting to pop or peek an element from an empty stack.
# Using exceptions allows for better error handling and control in exceptional cases.
