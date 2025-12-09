class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        prereqMap = defaultdict(list)
        for course, prereq in prerequisites:
            prereqMap[course].append(prereq)

        visit = set()
        def dfs(course):
            if course in visit:
                return False

            visit.add(course)
            for prereq in prereqMap[course]:
                if not dfs(prereq):
                    return False
            visit.remove(course)
            prereqMap[course] = []
            return True

        for course in range(numCourses):
            if not dfs(course):
                return False

        return True

