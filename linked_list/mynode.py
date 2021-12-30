class node:
    def __init__(self, item):
        self.data = item
        self.next = None

    def setData(self, item):
        self.data = item

    def setNext(self, target):
        self.next = target


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

