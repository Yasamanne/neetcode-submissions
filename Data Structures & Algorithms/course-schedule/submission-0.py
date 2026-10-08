class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        m = defaultdict(list)
        for c, p in prerequisites:
            m[c].append(p)

        visited = set()

        def dfs(crs):
            if crs in visited:
                return False
            if m[crs] == []:
                return True
            
            visited.add(crs)
            for pre in m[crs]:
                if not dfs(pre): return False
            visited.remove(crs)
            m[crs] = []
            return True

        for crs in range(numCourses):
            if not dfs(crs): return False
        return True