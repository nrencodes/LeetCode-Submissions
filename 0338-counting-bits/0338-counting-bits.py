class Solution:
    def countBits(self, n: int) -> List[int]:
        res = []
        for i in range(n + 1):
            curr = i
            zeroes = 0
            while curr:
                zeroes += curr % 2
                curr = curr >> 1
            res.append(zeroes)

        return res

        