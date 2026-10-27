class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        def normalize(word):
            t = [0]*26
            for letter in word:
                t[ord(letter)-97] += 1
            return t

        mem = []
        res=[]
        for item in strs:
            n = normalize(item)
            if n not in mem:
                mem.append(n)
                res.append([item])
            else:
                res[mem.index(n)].append(item)
        return res