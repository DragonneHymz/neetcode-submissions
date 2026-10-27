class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        
        MAX_ROW = len(heights)
        MAX_COL = len(heights[0])
        pacific_reachable = set()
        atlantic_reachable = set()

        def dfs(r,c,visited,prev_height):
            #check if out of bounds, if already visited, and if lower
            if (not 0 <= r < MAX_ROW) or (not 0 <= c < MAX_COL) or ((r,c) in visited) or (heights[r][c] < prev_height):
                return
            
            #if can climb up
            visited.add((r,c))

            #search in all four directions
            dfs(r+1,c,visited,heights[r][c])
            dfs(r-1,c,visited,heights[r][c])
            dfs(r,c+1,visited,heights[r][c])
            dfs(r,c-1,visited,heights[r][c])
        
        for r in range(MAX_ROW):
            dfs(r,0,pacific_reachable, heights[r][0])
            dfs(r,MAX_COL-1,atlantic_reachable, heights[r][MAX_COL-1])
            
        for c in range(MAX_COL):
            dfs(MAX_ROW-1,c,atlantic_reachable, heights[MAX_ROW-1][c])
            dfs(0,c,pacific_reachable, heights[0][c])

        #return if in both pacific and atlantic sets
        return list(pacific_reachable.intersection(atlantic_reachable))



        