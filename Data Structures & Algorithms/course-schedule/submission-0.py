class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        map = {i:[] for i in range(numCourses)}
        visited = set()
        for course, pre in prerequisites:
            map[course].append(pre)
        
        def dfs(course):
            if course in visited:
                return False
            if map[course] == []:
                return True
            visited.add(course)

            for n in map[course]:
                if not dfs(n):
                    return False
            
            visited.remove(course)
            map[course] = []
            return True

        for course in range(numCourses):
            if not dfs(course):
                return False
        return True


        