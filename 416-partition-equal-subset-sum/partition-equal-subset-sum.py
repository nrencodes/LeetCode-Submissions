class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2:
            return False

        target = sum(nums) // 2
        dp = set()
        dp.add(0)

        for i in range(len(nums)):
            nextDP = dp.copy()
            for n in dp:
                if(n + nums[i] == target):
                    return True
                nextDP.add(n + nums[i])
            dp = nextDP
        return True if target in dp else False