from linked_list import LinkedList

class HashTable:
    """
    Hash table for an asset cache system.
    Stores shot-task keys and maps them to asset paths.
    Uses separate chaining (linked lists) to handle collisions.
    """

    def __init__(self, size=50):
        # create a list of empty linked lists (buckets)
        self.size = size
        self.buckets = [LinkedList() for _ in range(self.size)]

    def _hash(self, key):
        # hash the key and map it to a bucket index
        return hash(key) % self.size

    def put(self, key, value):
        # add the key-value pair to the right bucket
        index = self._hash(key)
        self.buckets[index].insert(key, value)

    def get(self, key):
        # look up the key in the right bucket and return its value
        index = self._hash(key)
        return self.buckets[index].find(key)

    def delete(self, key):
        # remove the key-value pair from the right bucket
        index = self._hash(key)
        return self.buckets[index].delete(key)
    
    def display(self):
        """
        Prints out all key-value pairs in the hash table, bucket by bucket.
        Useful for debugging and understanding how the data is distributed across buckets.
        """
        print("\nCache Contents:")
        for i, bucket in enumerate(self.buckets):
            current = bucket.head
            if current:
                print(f"Bucket {i}:")
                while current:
                    print(f"  {current.key} → {current.value}")
                    current = current.next
