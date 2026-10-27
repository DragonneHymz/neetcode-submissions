class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        # create adjacency map
        adj = { c:set() for w in words for c in w}

        # put stuff in adj
        for w in range(len(words)-1):
            w1, w2 = words[w], words[w+1]
            minLength = min(len(w1), len(w2))
            if len(w1) > len(w2) and w1[:minLength] == w2[:minLength]:
                return ""
            for i in range(minLength):
                if w1[i] != w2[i]:
                    adj[w1[i]].add(w2[i])
                    break
        
        visited = {}
        res = []
        # dfs
        def dfs(node):
            # check for cycle
            if node in visited:
                return visited[node]
            visited[node] = True
            
            # recurse
            for neighbor in adj[node]:
                if dfs(neighbor):
                    return True
            
            # backtracking
            visited[node] = False

            # add to results
            res.append(node)
            return False
        
        for node in adj:
            if dfs(node):
                return ""
        
        res.reverse()
        return "".join(res)

        



        