class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        graph = [[0 for _ in range(len(text2)+1)] for _ in range(len(text1)+1)]
        
        for i in range(len(text1) -1, -1, -1):
            for j in range(len(text2)-1, -1, -1):
                if text1[i] == text2[j]:
                    graph[i][j] = 1+graph[i+1][j+1]
                else:
                    graph[i][j] = max(graph[i+1][j], graph[i][j+1])
        return graph[0][0]