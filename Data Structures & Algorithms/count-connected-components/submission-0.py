class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        hashMap = { i:[] for i in range(n) }
        visited = set()

        # store in adjacency list
        for e1,e2 in edges:
            hashMap[e1].append(e2)
            hashMap[e2].append(e1)

        # dfs
        def dfs(node):
            for neighbor in hashMap[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    dfs(neighbor)
        res=0
        for i in range(n):
            if i not in visited:
                dfs(i)
                res+=1
        return res
        

            
            

        
