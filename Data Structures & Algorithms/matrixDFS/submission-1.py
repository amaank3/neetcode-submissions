class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        return self.dfs(grid, 0, 0, set())

    def dfs(self, grid, r, c, visited):
        rows, cols = len(grid), len(grid[0])

        # Out of bounds, blocked, or visited
        if (r < 0 or r >= rows or c < 0 or c >= cols or
            grid[r][c] == 1 or (r, c) in visited):
            return 0

        # Reached bottom-right corner
        if r == rows - 1 and c == cols - 1:
            return 1

        visited.add((r, c))

        count = 0
        count += self.dfs(grid, r + 1, c, visited)
        count += self.dfs(grid, r - 1, c, visited)
        count += self.dfs(grid, r, c + 1, visited)
        count += self.dfs(grid, r, c - 1, visited)

        visited.remove((r, c))  # backtrack!

        return count
