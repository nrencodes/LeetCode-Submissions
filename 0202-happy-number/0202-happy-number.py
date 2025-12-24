class Solution:
    def isHappy(self, n: int) -> bool:
        def next_num(x) -> int:
            currSum = 0
            for integer in str(x):
                currSum += pow(int(integer), 2)
            return currSum

        first, second = n, next_num(n)

        while first != 1 and first != second: 
            first = next_num(first)
            second = next_num(next_num(second))

        return first == 1