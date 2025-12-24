class Solution:
    def isHappy(self, n: int) -> bool:
        sums = set()

        while n != 1:
            currSum = 0
            for integer in str(n):
                currSum += pow(int(integer), 2)

            if currSum in sums:
                return False

            n = currSum
            sums.add(currSum)

        return True