class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [0] * (n + 1)
        dp[0] = 1
        dp[1] = 1
        for i in range(2, n + 1):
            dp[i] = dp[i-1] + dp[i-2]

        return dp[n]

'''
    n = 1
    1. 1 step

    n = 2
    1. 1 step + 1 step
    2. 2 steps

    n = 3
    1. 1 step + 1 step + 1 step
    2. 2 steps + 1 step
    3. 1 step + 2 steps

    n = 4 
    1. 1 step + 1 step + 1 step + 1 step
    2. 2 steps + 2 steps
    3. 1 step + 2 steps + 1 step
    4. 1 step + 1 step + 2 steps
    5. 2 steps + 1 step + 1 step

    n = 5
    1. 1 step + 1 step + 1 step + 1 step + 1 step
    2. 2 steps + 2 steps + 1 step
    3. 2 steps + 1 step + 1 step + 1 step
    4. 1 step + 2 steps + 1 step + 1 step
    5. 1 step + 1 step + 2 steps + 1 step
    6. 1 step + 1 step + 1 step + 2 steps
    7. 2 steps + 1 step + 2 steps
    8. 1 step + 2 steps + 2 steps

'''
