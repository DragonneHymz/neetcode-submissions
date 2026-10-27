class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        quadrants = {}
        rows = {}
        columns = {}
        
        for row in range(len(board)):
            for column in range(len(board[0])):
                if board[row][column] == ".":
                    continue
                    
                value = board[row][column]
                quadrant = (row // 3, column // 3)
                
                # Check if value already exists in its quadrant, row, or column
                if (value in quadrants.get(quadrant, set()) or
                    value in rows.get(row, set()) or
                    value in columns.get(column, set())):
                    return False
                
                # Update sets
                quadrants[quadrant] = quadrants.get(quadrant, set()) | {value}
                rows[row] = rows.get(row, set()) | {value}
                columns[column] = columns.get(column, set()) | {value}
        
        return True