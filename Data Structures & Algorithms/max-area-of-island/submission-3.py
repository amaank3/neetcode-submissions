class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        visits = set()
        max_area = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and (r,c) not in visits:
                    current_area = self.dfs(grid,r,c,visits)
                    max_area = max(max_area, current_area)
        return max_area



    def dfs(self,grid,r,c,visits):
        rows, cols = len(grid), len(grid[0])

        if min(r,c) < 0 or r == rows or c == cols or grid[r][c] == 0 or (r,c) in visits:
            return 0


        visits.add((r,c))

        area = 1

        area+= self.dfs(grid,r+1,c,visits)
        area+= self.dfs(grid,r-1, c, visits)
        area+= self.dfs(grid, r, c+1, visits)
        area+= self.dfs(grid,r,c-1,visits)

        return area

        