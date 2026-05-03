from collections import deque

class Queue:
    def __init__(self):
        self.elements = deque()

    def push(self, element):
        self.elements.append(element)

    def pop(self):
        if self.is_empty():
            raise IndexError("pop from empty queue")
        return self.elements.popleft()

    def peek(self):
        if self.is_empty():
            raise IndexError("peek from empty queue")
        return self.elements[0]

    def is_empty(self):
        return len(self.elements) == 0

    def size(self):
        return len(self.elements)

    def __len__(self):
        return len(self.elements)

    def __repr__(self):
        return f"Queue({list(self.elements)})"
