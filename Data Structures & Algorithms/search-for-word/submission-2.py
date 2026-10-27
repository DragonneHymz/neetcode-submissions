class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def dfs(r,c,index):
            if index == len(word):
                return True

            if not 0<=r<len(board) or not 0<=c<len(board[r]) or board[r][c] == "#" or board[r][c] != word[index]:
                return False

            char = board[r][c]
            board[r][c] = "#"

            if dfs(r+1,c,index+1) or dfs(r-1,c,index+1) or dfs(r,c+1,index+1) or dfs(r,c-1,index+1):
                return True

            board[r][c] = char

        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == word[0]:
                    if dfs(i,j,0):
                        return True
        
        return False




            
