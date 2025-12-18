class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0

        for i in range(32):
            # Find the bit in the ones place 
            bit = n & 1
            n >>= 1

            # shift result 1 to the left and then or with current bit
            res = (res << 1) | bit
            
        return res