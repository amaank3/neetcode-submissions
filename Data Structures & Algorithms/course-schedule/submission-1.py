class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = self.buildGraph(numCourses, prerequisites)
        visited = set()
        path = set()

        for course in range(numCourses):
            if course not in visited:
                if self.hasCycle(course, graph, visited, path):
                    return False
        return True
        
    def hasCycle(self, node, graph, visited, path):
        
        if node in path:
            return True
        if node in visited:
            return False
        
        path.add(node)
        for neighbor in graph[node]:
            if self.hasCycle(neighbor, graph, visited, path):
                return True
        path.remove(node)
        visited.add(node)
        return False

    

    def buildGraph(self, numCourses: int, prerequisites: List[List[int]]) -> dict[int, List[int]]:
        graph = {}
        for i in range(numCourses):
            graph[i] = []
        for course, prereq in prerequisites:
            graph[prereq].append(course)
        return graph


        