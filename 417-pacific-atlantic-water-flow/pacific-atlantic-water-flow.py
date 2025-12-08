class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        p_q, a_q = deque(), deque()
        p_visit, a_visit = set(), set()
        m, n = len(heights), len(heights[0])

        # top row   
        for col in range(n):
            p_q.append((0, col))
            p_visit.add((0, col))

        # left column
        for row in range(1, m):
            p_q.append((row, 0))
            p_visit.add((row, 0))

        # bottom row
        for col in range(n):
            a_q.append((m - 1, col))
            a_visit.add((m - 1, col))

        # right column
        for row in range(m - 1):
            a_q.append((row, n - 1))
            a_visit.add((row, n - 1))

        def bfs(queue, visited):
            while queue:
                r, c = queue.popleft()
                for i, j in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                    nr, nc = r+i, c+j
                    if 0 <= nr < m and 0 <= nc < n and heights[nr][nc] >= heights[r][c] and (nr, nc) not in visited:
                        queue.append((nr, nc))
                        visited.add((nr, nc))
            return visited

        pacific = bfs(p_q, p_visit)
        atlantic = bfs(a_q, a_visit)
        return list(pacific.intersection(atlantic))