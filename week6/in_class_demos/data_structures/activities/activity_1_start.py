# # Challenge 1 - Instructions
# A stack is a last-in, first-out (LIFO) data structure that allows elements to be 
# inserted and removed from the same end, called the top of the stack. 
# Your task is to create a Python class named Stack with the following methods:

# __init__: Initializes an empty stack.

# push(item): Adds an item to the top of the stack.
# pop(): Removes and returns the item at the top of the stack. 

# If the stack is empty, it returns None.
# is_empty(): Returns True if the stack is empty, False otherwise.

class Stack:
    def __init__(self):  # __init__: Initializes an empty stack
        self.stack = []

    def push(self, item):  # push(item): Adds an item to the top of the stack.
        self.stack.append(item)

    def pop(self):  # pop(): Removes and returns the item at the top of the stack.
        if self.is_empty():
            return None
        elif not self.is_empty():
            return self.stack.pop()

    def is_empty(self):  # is_empty(): Returns True if the stack is empty, False otherwise.
        if not self.stack:
            return True
        else:
            return False
