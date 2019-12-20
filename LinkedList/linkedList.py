class Node:
    def __init__(self, x = 0):
        self.data = x
        self.next = None

class LinkedList:
    def __init__(self):
        self.header = None
        self.tail = None