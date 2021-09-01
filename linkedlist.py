class LinkedList:
    def __init__(self, last=None, data=None):
        self.data = data
        self.last = last
        self.next = None

    def _is_tail(self):
        return True if self.next is None else False

    def _is_head(self):
        return True if self.last is None else False

    def insert(self, new_data):
        if self.data is None:
            self.data = new_data
            return

        if self.next is None:
            self.next = LinkedList(self, new_data)
        else:
            self.next.extend_list(new_data)

