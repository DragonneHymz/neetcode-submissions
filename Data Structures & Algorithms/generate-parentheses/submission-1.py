class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        current = []

        def backtrack(openP, closedP):
            if openP==n and closedP==n:
                res.append("".join(current))
            
            if openP < n:
                current.append("(")
                backtrack(openP+1, closedP)
                current.pop()
            
            if closedP < openP:
                current.append(")")
                backtrack(openP, closedP+1)
                current.pop()
        
        backtrack(0,0)
        return res
        