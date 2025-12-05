class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.kNums = nums
        heapq.heapify(self.kNums)
        while len(self.kNums) > k:
            heapq.heappop(self.kNums)

    def add(self, val: int) -> int:
        heapq.heappush(self.kNums, val)
        if len(self.kNums) > self.k:
            heapq.heappop(self.kNums)

        return self.kNums[0]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)