class SymbolTable:

    class Node:
        def __init__(self, key, value):
            self.key = key
            self.value = value
            self.next = None

    def __init__(self, capacity):
        self.table = [None] * capacity
        self.size = 0
        self.capacity = capacity

    def hash(self, key):
        hashsum = 0

        for idx, c in enumerate(key):
            hashsum += (idx + len(key)) ** ord(c)
            hashsum = hashsum % self.capacity

    def insert(self, key, value):
        self.size += 1
    

def main():
    pass

if __name__ == "__main__":
    main()
