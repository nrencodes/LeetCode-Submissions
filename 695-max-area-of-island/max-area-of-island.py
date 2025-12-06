class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        ROWS, COLS = len(grid), len(grid[0])
        maxArea = 0

        def bfs(r, c):
            queue = deque()
            grid[r][c] = 0
            queue.append((r, c))
            area = 1

            while queue:
                r, c = queue.popleft()
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if(nr < 0 or nc < 0 or 
                       nr >= len(grid) or nc >= len(grid[0])
                       or grid[nr][nc] == 0):
                       continue
                    queue.append((nr, nc))   
                    grid[nr][nc] = 0
                    area += 1
                    print(area)
            return area

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:

                    maxArea = max(maxArea, bfs(r, c))

        return maxArea