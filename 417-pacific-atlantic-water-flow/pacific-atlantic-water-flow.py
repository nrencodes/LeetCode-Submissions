class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        height, width = len(heights), len(heights[0])
        pacific, atlantic = set(), set()

        def dfs(i, j, visit, num):
            if ((i, j) in visit or
            i < 0 or i >= height or
            j < 0 or j >= width or
            heights[i][j] < num):
                return

            visit.add((i, j))
            for nr, nc in [(-1,0),(1,0),(0,1),(0,-1)]:
                dfs(i + nr, j + nc, visit, heights[i][j])


        for i in range(height):
            dfs(i, 0, pacific, heights[i][0])
            dfs(i, width - 1, atlantic, heights[i][width-1])

        for i in range(width):
            dfs(0, i, pacific, heights[0][i])
            dfs(height-1, i, atlantic, heights[height-1][i])

        return list(pacific & atlantic)
            


        