class Graph:
    
    def __init__(self):
        self.graph_map = {}


    def addEdge(self, src: int, dst: int) -> None:
        if src not in self.graph_map:
            self.graph_map[src]=[]
        if dst not in self.graph_map:
            self.graph_map[dst]=[]
        self.graph_map[src].append(dst)

    def removeEdge(self, src: int, dst: int) -> bool:
        if src not in self.graph_map:
            return False
        if dst not in self.graph_map:
            return False
        self.graph_map[src].remove(dst)  
        return True    

    def hasPath(self, src: int, dst: int) -> bool:
        if src not in self.graph_map or dst not in self.graph_map:
            return False  # safeguard for unknown nodes
        visit = set()
        return self.dfs(src, dst, visit)

    def dfs(self, src, dst, visit):
        if src == dst:
            return True
        if src in visit:
            return False

        visit.add(src)

        for neighbor in self.graph_map.get(src, []):
            if self.dfs(neighbor, dst, visit):
                return True

        return False

        # length = 0
        # visit = set()
        # visit.add(src)
        # queue = deque()
        # queue.append(src)

        # while queue:
        #     for i in range(len(queue)):
        #         curr = queue.popleft()
        #         if curr == dst:
        #             return True
                
        #     for neighbour in self.graph_map[curr]:
        #         if neigbour not in visit:
        #             visit.add(neighbour)
        #             queue.append(neghbour)







