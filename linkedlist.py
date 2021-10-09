class Node:
    """
    A node for use in linked lists.
    """
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    def set_next(self, new_next):
        if new_next is None or isinstance(new_next, Node):
            self.next = new_next
        else:
            raise TypeError('Nodes can only be attached to other nodes or to the None object')


class LinkedList():
    """
    A singly linked list implementation. Iterable.
    """
    def __init__(self, head=None):
        if head is None:
            head = Node(None)
        if isinstance(head, Node):
            self.head = head
        else:
            raise TypeError('Linked list head must be a node')

    def is_empty(self):
        return self.head.value is None

    def __iter__(self):
        if self.is_empty():
            yield None
        else:
            curr_node = self.head
            while curr_node is not None:
                yield curr_node.value
                curr_node = curr_node.next

    def __len__(self):
        if self.is_empty():
            return 0
        else:
            return sum([1 for _ in self])

    def insert(self, value):
        if self.is_empty():
            self.head.value = value
            return self

        curr_node = self.head
        while curr_node.next is not None:
            curr_node = curr_node.next
        curr_node.next = Node(value)
        return self

    def pop(self):
        if self.head.next is None:
            return self.head.value

        last_node = None
        curr_node = self.head
        while curr_node.next is not None:
            last_node = curr_node
            curr_node = curr_node.next

        last_node.set_next(None)
        return curr_node.value






