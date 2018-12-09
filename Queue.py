class Queue:
    def __init__(self):
        self.elements = []

    def push(self, element):
        self.elements.append(element)

    def pop(self):
        return self.elements.pop(0)

    def peek(self):
        return self.elements[0]

    def isEmpty(self):
        if len(self.elements) == 0:
            return True
        else:
            return False

    def size(self):
        return len(self.elements)
