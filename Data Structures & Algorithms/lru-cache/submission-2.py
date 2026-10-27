class Node:
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.prev = self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cache, self.capacity = {}, capacity
        self.leftNode, self.rightNode = Node(0,0), Node(0,0)
        self.leftNode.next, self.rightNode.prev = self.rightNode, self.leftNode

    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])
        if len(self.cache) > self.capacity:
            # 1. Store the LRU node in a temporary variable
            lru = self.leftNode.next
            
            # 2. Remove it from the list
            self.remove(lru)
            
            # 3. Delete it from the dictionary using the stored reference
            del self.cache[lru.key]

    
    def remove(self, node: Node):
        node.prev.next, node.next.prev = node.next, node.prev
    
    def insert(self, node: Node):
        # Identify the neighbors
        prev, nxt = self.rightNode.prev, self.rightNode
        
        # Link the neighbors to the new node
        prev.next = nxt.prev = node
        
        # Link the new node to the neighbors
        node.prev, node.next = prev, nxt
        
