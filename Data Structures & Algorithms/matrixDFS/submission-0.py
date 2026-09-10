class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        return self.dfs(grid,0,0,set())


    def dfs(self,grid,r,c,visits):
        rows = len(grid)
        columns = len(grid[0])

        if min(r,c) < 0 or r == rows or c == columns or grid[r][c]==1 or (r,c) in visits:
            return 0
        
        if r == rows-1 and c == columns-1:
            return 1

        visits.add((r,c))

        count = 0
        count+= self.dfs(grid,r+1,c,visits)
        count+= self.dfs(grid,r-1,c,visits)
        count+= self.dfs(grid,r,c+1,visits)
        count+= self.dfs(grid,r,c-1,visits)

        visits.remove((r,c))

        return count

        