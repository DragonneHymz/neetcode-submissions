class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLUMNS = len(grid), len(grid[0])
        res = -1
        total = 0
        rotten = 0
        q = collections.deque()
        for i in range(ROWS):
            for j in range(COLUMNS):
                if grid[i][j] == 2:
                    q.append((i,j))
                    rotten += 1
                if grid[i][j] > 0:
                    total += 1
        while q:
            for _ in range(len(q)):
                currentRow, currentCol = q.popleft()
                if currentRow+1<ROWS and grid[currentRow+1][currentCol] == 1:
                    q.append((currentRow+1, currentCol))
                    grid[currentRow+1][currentCol] = 2
                    rotten += 1
                if currentRow-1 > -1 and grid[currentRow-1][currentCol] == 1:
                    q.append((currentRow-1, currentCol))
                    grid[currentRow-1][currentCol] = 2
                    rotten += 1
                if currentCol+1 < COLUMNS and grid[currentRow][currentCol+1] == 1:
                    q.append((currentRow, currentCol+1))
                    grid[currentRow][currentCol+1] = 2
                    rotten += 1
                if currentCol-1 > -1 and grid[currentRow][currentCol-1] == 1:
                    q.append((currentRow, currentCol-1))
                    grid[currentRow][currentCol-1] = 2
                    rotten += 1
            res += 1
        
        return max(res, 0) if total == rotten else -1


