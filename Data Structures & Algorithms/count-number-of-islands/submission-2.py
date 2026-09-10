class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visits = set()
        rows, cols = len(grid), len(grid[0])
        count = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1' and (r, c) not in visits:
                    self.dfs(grid, r, c, visits)
                    count+=1
        return count
                





    def dfs(self, grid, r, c, visited):
        rows, cols = len(grid), len(grid[0])

        if (r < 0 or r >= rows or c < 0 or c >= cols or
            grid[r][c] == '0' or (r, c) in visited):

            return

        visited.add((r, c)) 

        self.dfs(grid, r + 1, c    , visited)
        self.dfs(grid, r - 1, c    , visited)
        self.dfs(grid, r    , c + 1, visited)
        self.dfs(grid, r    , c - 1, visited)


