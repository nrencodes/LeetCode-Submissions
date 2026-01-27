class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
            res, dists = [], []

            for point in points:
                x, y = point[0], point[1]
                dist = math.sqrt(x ** 2 + y ** 2)
                dists.append([dist, point])
            
            heapq.heapify(dists)

            for i in range(k):
                res.append(heapq.heappop(dists)[1])
            
            return res