class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(i, current, currSum):
            if currSum == target:
                res.append(current.copy())
                return
            if i >= len(candidates) or currSum > target:
                return

            #  Option 1: add current number to the tree
            current.append(candidates[i])
            dfs(i, current, currSum + candidates[i])

            # Option 2: skip current number, increment index and rest of numbers
            current.pop()
            dfs(i+1, current, currSum)

        dfs(0, [], 0)
        return res

