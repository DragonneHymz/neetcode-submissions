class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        def toAlph(s:str) -> []:
            res = [0]*26
            for i in range(len(s)):
                res[ord(s[i]) - ord('a')]+= 1
            return res


        front = 0
        back = len(s1)
        constant = toAlph(s1)
        while back <= len(s2):
            print(s2[front:back])
            if toAlph(s2[front:back]) == constant:
                return True
            front += 1
            back += 1
        
        return False
