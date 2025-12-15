class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        prereqMap = defaultdict(list)
        for course, prereq in prerequisites:
            prereqMap[course].append(prereq)

        visit = set()
        done = set()
        res = [] 
        def dfs(course):
            nonlocal res
            if course in visit:
                return False
            if course in done:
                return True

            visit.add(course)
            for prereq in prereqMap[course]:
                if not dfs(prereq):
                    return False
            visit.remove(course)
            done.add(course)
            res.append(course)
            return True

        for course in range(numCourses):
            if not dfs(course):
                return []

        return res