class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights:
            return []

        rows, cols = len(heights), len(heights[0])
        pacific = set()
        atlantic = set()

        for c in range(cols):
            self.dfs(0, c, pacific, heights, rows, cols, heights[0][c])
            self.dfs(rows - 1, c, atlantic, heights, rows, cols, heights[rows - 1][c])

        for r in range(rows):
            self.dfs(r, 0, pacific, heights, rows, cols, heights[r][0])
            self.dfs(r, cols - 1, atlantic, heights, rows, cols, heights[r][cols - 1])

        result = []
        for r in range(rows):
            for c in range(cols):
                if (r, c) in pacific and (r, c) in atlantic:
                    result.append([r, c])

        return result

    def dfs(self, r, c, visited, heights, rows, cols, prev_height):
        if (
            r < 0 or r >= rows or
            c < 0 or c >= cols or
            (r, c) in visited or
            heights[r][c] < prev_height
        ):
            return

        visited.add((r, c))

        self.dfs(r + 1, c, visited, heights, rows, cols, heights[r][c])
        self.dfs(r - 1, c, visited, heights, rows, cols, heights[r][c])
        self.dfs(r, c + 1, visited, heights, rows, cols, heights[r][c])
        self.dfs(r, c - 1, visited, heights, rows, cols, heights[r][c])
