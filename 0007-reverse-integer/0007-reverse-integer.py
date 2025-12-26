class Solution:
    def reverse(self, x: int) -> int:
        res = 0
        # check for sign 
        pos = x >= 0

        maxInt = 2**31 - 1
        x = abs(x)

        while x:
            curr = x % 10
            x = x // 10

            # need to check if the current number is over the overflow yet
            if res > maxInt // 10:
                return 0 
            elif res == maxInt // 10 and curr > (7 if pos else 8):
                return 0 
            res = (res * 10) + curr

        return res if pos else -res