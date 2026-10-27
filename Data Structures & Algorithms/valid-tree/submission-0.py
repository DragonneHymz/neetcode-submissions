class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if not n:
            return True
        
        hashMap = { i: [] for i in range(n)}
        for e,v in edges:
            hashMap[e].append(v)
            hashMap[v].append(e)
        
        visited = set()

        def dfs(node, prev):
            #base case
            if node in visited:
                return False
            #add in visited
            visited.add(node)
            # call dfs
            for neighbor in hashMap[node]:
                if neighbor == prev:
                    continue
                if not dfs(neighbor, node):
                    return False

            return True
        
        
        return dfs(0,-1) and len(visited) == n
