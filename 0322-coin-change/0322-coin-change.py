class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0

        for total in range(1, amount + 1):
            for currCoin in coins:
                if total - currCoin >= 0:
                    dp[total] = min(dp[total], 1 + dp[total - currCoin])

        return dp[amount] if dp[amount] != float('inf') else -1
