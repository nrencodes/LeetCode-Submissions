class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        visited, islands = set(), 0

        def BFS(i, j):
            queue = collections.deque()
            visited.add((i, j))
            queue.append((i, j))
            while queue:
                row, column = queue.popleft()
                directions = [[-1, 0],[1, 0],[0, -1],[0, 1]]
                for directionRow, directionColumn in directions:
                    r, c = row + directionRow, column + directionColumn
                    if (r in range(len(grid)) and
                        c in range(len(grid[0])) and
                        (r, c) not in visited and
                        grid[r][c] == "1"):
                        queue.append((r, c))
                        visited.add((r, c))

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                currNum = grid[i][j]
                if currNum == "1" and (i, j) not in visited:
                    BFS(i, j)
                    islands += 1
        return islands
        