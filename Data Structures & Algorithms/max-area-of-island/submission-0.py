class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        def dfs(r,c):
            area = 0
            if not 0 <= r < len(grid) or not 0 <= c < len(grid[0]) or grid[r][c] == 0:
                return area
            area += 1
            grid[r][c] = 0

            area += dfs(r+1, c)
            area += dfs(r-1, c)
            area += dfs(r, c+1)
            area += dfs(r, c-1)

            return area
        
        maxArea = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    maxArea = max(maxArea,dfs(i,j))
        
        return maxArea
