class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(r,c):
            if not 0<= r <len(grid) or not 0<= c <len(grid[r]) or grid[r][c] == "0":
                return
            
            grid[r][c] = "0"

            dfs(r+1,c)
            dfs(r-1,c)
            dfs(r,c+1)
            dfs(r,c-1)
        
        res = 0

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == "1":
                    res += 1
                    dfs(i,j)
        
        return res
