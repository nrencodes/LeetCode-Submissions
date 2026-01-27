class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        adjList = {i: [] for i in range(len(points))}
        for i in range(len(points)):
            for j in range(i+1, len(points)):
                dist = abs(points[j][0] - points[i][0]) + abs(points[j][1] - points[i][1])
                # add both ways to create an undirected graph
                adjList[i].append([dist, j])
                adjList[j].append([dist,i])
        
        res = 0
        visit = set()
        minq = [[0,0]] # start at first point in list with 0 cost [cost, index]
        while len(visit) < len(points):
            cost, index = heapq.heappop(minq)
            if index in visit:
                continue
            res += cost
            visit.add(index)
            for edgeWeight, nextPoint in adjList[index]:
                if nextPoint not in visit:
                    heapq.heappush(minq, [edgeWeight, nextPoint])

        return res