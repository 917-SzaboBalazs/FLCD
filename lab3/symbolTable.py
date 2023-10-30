class SymbolTable:

    class Node:
        def __init__(self, key, value):
            self._key = key
            self._value = value
            self._next = None

    def __init__(self, capacity=100):
        self._table = [None] * capacity
        self._size = 0
        self._capacity = capacity

    def __hash(self, key):
        return key % self.capacity()

    def insert(self, key, value):
        index = self.__hash(key)

        entry_point = self._table[index]

        if entry_point is None:
            self._table[index] = self.Node(key, value)
            self._size += 1
            return
        
        curr = entry_point
        prev = curr
        
        while curr is not None and curr._key != key:
            prev = curr
            curr = curr._next

        if curr is None:
            prev._next = self.Node(key, value)
            self._size += 1
        else:
            curr._value = value

    def find_by_value(self, value):
        for entry in self._table:
            curr = entry
            while curr is not None:
                if curr._value == value:
                    return curr._key, value
                curr = curr._next
        
        return None

    def find(self, key):
        index = self.__hash(key)

        curr = self._table[index]

        while curr is not None and curr._key != key:
            curr = curr._next

        return curr
    
    def remove(self, key):
        index = self.__hash(key)
        entry_point = self._table[index]

        curr = entry_point
        prev = None

        while curr is not None and curr._key != key:
            prev = curr
            curr = curr._next

        if curr is None:
            return None

        self._size -= 1
        result = curr._value

        if prev is None:
            self._table[index] = self._table[index]._next


        else:
            prev._next = prev._next._next

        return result
    
    def get_all(self):
        all_entries = []

        for entry in self._table:
            curr = entry
            while curr is not None:
                all_entries.append((curr._key, curr._value))
                curr = curr._next

        return all_entries
    
    def size(self):
        return self._size
    
    def capacity(self):
        return self._capacity
