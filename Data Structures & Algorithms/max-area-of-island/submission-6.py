class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        visits = set()
        max_area = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    current_area = self.dfs(grid,r,c, visits)
                    max_area = max(current_area, max_area)
        
        return max_area
                    



    def dfs(self, grid, r, c, visits):

        rows, cols = len(grid), len(grid[0])

        if (min(r,c)) < 0 or r == rows or c == cols or grid[r][c]==0 or (r,c) in visits:
            return 0

        visits.add((r,c))

        count = 1
        count+= self.dfs(grid,r+1,c,visits)
        count+= self.dfs(grid,r-1,c,visits)
        count+= self.dfs(grid,r,c+1,visits)
        count+= self.dfs(grid,r,c-1,visits)

        return count

        