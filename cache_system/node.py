class Node:
    """
    Represents a single key-value pair in the cache.
    Used as a node in the LinkedList for collision handling.
    """
    def __init__(self, key, value):
        self.key = key          # unique identifier for the asset (e.g., "SHOT_014_ANIM")
        self.value = value      # file path or other asset data
        self.next = None        # pointer to the next node in the list (for chaining)
