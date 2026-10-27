class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        quadrants = {}
        rows = {}
        columns = {}
        for row in range(len(board)):
            for column in range(len(board[0])):
                if board[row][column] != ".":
                    if ((row//3, column//3) in quadrants.keys()) and (board[row][column] in quadrants[row//3, column//3]):
                        return False
                    else:
                        quadrants[(row//3, column//3)] = quadrants.get((row//3, column//3),set()) | {board[row][column]}
                    if (row in rows.keys()) and (board[row][column] in rows[row]):
                        return False
                    else:
                        rows[row] = rows.get(row,set()) | {board[row][column]}
                    if (column in columns.keys()) and (board[row][column] in columns[column]):
                        return False
                    else:
                        columns[column] = columns.get(column,set()) | {board[row][column]}
        return True