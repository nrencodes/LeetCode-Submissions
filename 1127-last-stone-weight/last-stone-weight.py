class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        max_heap = []
        for stone in stones:
            heapq.heappush(max_heap, -stone)

        print(max_heap)

        while len(max_heap) > 1:
            first, second = -heapq.heappop(max_heap), -heapq.heappop(max_heap)
            if first != second:
                heapq.heappush(max_heap, second - first)
        
        return 0 if len(max_heap) == 0 else -max_heap[0] 
                

        