# TODO: Separate functionaliy between a node class and a class for entire lists

class LinkedList:
    def __init__(self, last=None, data=None):
        self.data = data
        self.last = last
        self.next = None

    def _is_tail(self):
        return True if self.next is None else False

    def _is_head(self):
        return True if self.last is None else False

    def get_head(self):
        if self._is_head():
            return self
        else:
            return self.last.get_head()

    def insert(self, new_data):  # note: insertion works with the whole list, not just a node
        if self.data is None:
            self.data = new_data
            return

        if self.next is None:
            self.next = LinkedList(self, new_data)
        else:
            self.next.insert(new_data)

    def delete(self):
        '''
        This is where things get ugly with my design. After this, the calling instance is garbage, and should be
        reassigned to the return of the method call (which is the head of the linked list after deleting the calling
        node).
        '''
        self.data = None
        if not self._is_tail():
            self.next.last = self.last
        if not self._is_head():
            self.last.next = self.next

        if not self._is_tail(): # This is needed in case you are the head but not the tail
            return self.next.get_head()
        else:
            return self.get_head()

    def __iter__(self):  # note: Includes previous elements in the list
        current_node = self.get_head()
        while current_node:
            yield current_node
            current_node = current_node.next

    def search(self, bool_func):
        for node in self:
            if bool_func(node.data):
                return node.data

    def __contains__(self, item):
        for node in self:
            # TODO: stop making assumptions about data without enforcing them
            if node.data is not None and node.data[0] == item:
                return True

        return False

    def __str__(self):
        string = ''
        for node in self:
            string += f'{node.data} --> '

        return string[:len(string)-5]


if __name__ == "__main__":
    example = LinkedList(data=1)
    for x in range(2, 50):
        example.insert(x)

    print(example)
    five = example.search(bool_func=lambda x: x**2 == 25)
    print(five)

    example = example.next.next.next

    example = example.delete()
    print(example)
