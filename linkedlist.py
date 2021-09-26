class Node:
    def __init__(self, value, previous=None, next=None):
        self.value = value
        self.prev = previous
        self.next = next

    def set_next(self, new_next):
        if new_next is None:
            self.next = new_next
        elif isinstance(new_next, Node):
            self.next = new_next
            new_next.prev = self
        else:
            raise TypeError('Nodes can only be attached to other nodes or to the None object')


class LinkedList:
    def __init__(self, head=Node(None)):
        if isinstance(head, Node):
            self.head = head
        else:
            raise TypeError('Linked list head must be a node')

    def is_empty(self):
        return self.head.value is None

    def __iter__(self):

