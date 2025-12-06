class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        kNums = nums
        heapq.heapify(kNums)
        while len(kNums) > k:
            heapq.heappop(kNums)
        
        return kNums[0]


