from linked_list import LinkedList

class HashTable:
    """
    Hash table implementation for an asset cache system.
    Maps shot-task keys to asset paths using separate chaining for collision handling.
    """
    def __init__(self, size=50):
        self.size = size
        self.buckets = [LinkedList() for _ in range(self.size)]

    def _hash(self, key):
        # simple hashing based on built-in hash function
        return hash(key) % self.size

    def put(self, key, value):
        index = self._hash(key)
        self.buckets[index].insert(key, value)

    def get(self, key):
        index = self._hash(key)
        return self.buckets[index].find(key)

    def delete(self, key):
        index = self._hash(key)
        return self.buckets[index].delete(key)
    
    def display(self):
        """
        Prints out all key-value pairs in the hash table, bucket by bucket.
        """
        print("\nCache Contents:")
        for i, bucket in enumerate(self.buckets):
            current = bucket.head
            if current:
                print(f"Bucket {i}:")
                while current:
                    print(f"  {current.key} → {current.value}")
                    current = current.next
