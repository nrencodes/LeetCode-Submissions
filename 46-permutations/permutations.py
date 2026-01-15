class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        length = len(nums)
        res, curr = [], []

        def dfs():
            if len(curr) == length:
                res.append(curr.copy())
                return
            
            for n in nums:
                if n not in curr:
                    curr.append(n)
                    dfs()
                    curr.pop()

        dfs()
        return res