class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        current = "("
        def isValid(current):
            return current.count("(") >= current.count(")")
        
        def isFinal(current):
            return current.count("(") == current.count(")")

        def checkIfValid(current):
            if len(current) == 2*n:
                if isFinal(current) and current not in res:
                    res.append(current)
                return;

            lcurrent = current + "("
            rcurrent = current + ")"

            if isValid(lcurrent):
                checkIfValid(lcurrent)

            if isValid(rcurrent):
                checkIfValid(rcurrent)

        checkIfValid(current)
        return res

