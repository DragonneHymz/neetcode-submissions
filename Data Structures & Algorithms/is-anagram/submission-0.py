class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        sdict = {}
        for letter in s:
            if letter not in sdict.keys():
                sdict[letter] = s.count(letter)
        for letter in t:
            if letter not in sdict.keys():
                return False
            if sdict[letter] != t.count(letter):
                return False
        return True
