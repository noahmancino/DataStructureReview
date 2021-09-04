from linkedlist import LinkedList

class HashTable:
    class ClosedHashTable:
        def __init__(self, size):
            self.table = [LinkedList() for _ in range(50)]
            self.size = size
            self.entries = 0

        def _hash(self, key):
            return hash(key) % self.size

        def insert(self, key, value):
            if
            self.table[self._hash(key)].insert((key, value))
