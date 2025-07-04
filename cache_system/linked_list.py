from node import Node

class LinkedList:
    """
    Handles collisions in the hash table using separate chaining.
    Each bucket in the hash table points to a linked list of key-value pairs.
    """
    def __init__(self):
        # start with an empty list
        self.head = None

    def insert(self, key, value):
        # update value if key already exists
        current = self.head
        while current:
            if current.key == key:
                current.value = value
                return
            current = current.next

        # otherwise, insert new node at the beginning
        new_node = Node(key, value)
        new_node.next = self.head
        self.head = new_node

    def find(self, key):
        # search for a node with the matching key
        current = self.head
        while current:
            if current.key == key:
                return current.value
            current = current.next
        return None

    def delete(self, key):
        # remove node with matching key, if it exists
        current = self.head
        prev = None
        while current:
            if current.key == key:
                if prev:
                    prev.next = current.next
                else:
                    self.head = current.next
                return True
            prev = current
            current = current.next
        return False
