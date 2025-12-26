class DetectSquares:

    def __init__(self):
        self.points = defaultdict(int)

    def add(self, point: List[int]) -> None:
        self.points[tuple(point)] += 1

    def count(self, point: List[int]) -> int:
        res = 0
        px, py = point
        for x, y in self.points:
            if (abs(px - x) != abs(py - y)) or (x == px and y == py):
                continue
            if (px, y) in self.points and (x, py) in self.points:
                res += self.points[(px, y)] * self.points[(x, py)] * self.points[(x, y)] 
        return res


# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)