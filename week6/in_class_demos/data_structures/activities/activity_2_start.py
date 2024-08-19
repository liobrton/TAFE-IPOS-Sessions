# Challenge 2 - Instructions
# A queue is a first-in, first-out (FIFO) data structure that allows elements to be 
# inserted and removed from opposite ends, called the front of the queue. 

# Your task is to create a Python class named Queue with the following methods:

# __init__: Initializes an empty stack.
# push(item): Adds an item to the top of the stack.
# pop(): Removes and returns the item at the front of the queue.

# If the queue is empty, it returns None.
# peek(): Returns the item at the front of the queue without removing it

# If the queue is empty, it returns None.
# is_empty(): Returns True if the queue is empty, False otherwise.

from collections import deque


class Queue:
    def __init__(self):
        self.queue = deque()

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if self.is_empty():
            return None
        elif not self.is_empty():
            return self.queue.popleft()

    def peek(self):
        if self.is_empty():
            return None
        elif not self.is_empty():
            return self.queue[0]

    def is_empty(self):
        if not self.queue:
            return True
        else:
            return False