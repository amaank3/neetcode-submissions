class Node:
    def __init__(self, key, val):
        self.prev = None
        self.next = None
        self.val = val
        self.key = key

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}  

        self.left = Node(0, 0)  
        self.right = Node(0, 0) 
        self.left.next = self.right
        self.right.prev = self.left

    # Remove a node from the DLL
    def remove(self, node):
        prev_node = node.prev
        next_node = node.next
        prev_node.next = next_node
        next_node.prev = prev_node

    def insert(self, node):
        prev_node = self.right.prev
        prev_node.next = node
        node.prev = prev_node
        node.next = self.right
        self.right.prev = node

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

        if len(self.cache) > self.cap:
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]
        
