class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        prereqs = defaultdict(list)
        # 11/20/24) Wed) 1144-1156pm) tk) 12th problem of the day done
        for course, pre in prerequisites:
            prereqs[course].append(pre)

        took = set()

        def dfs(course):
            if not prereqs[course]:
                return True
            if course in took:
                return False
            took.add(course)
            for p in prereqs[course]:
                if not dfs(p):
                    return False
            prereqs[course] = []
            return True
        for course in range(numCourses):
            if not dfs(course):
                return False
        return True