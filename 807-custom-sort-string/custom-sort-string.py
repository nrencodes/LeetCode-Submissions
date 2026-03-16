class Solution:
    def customSortString(self, order: str, s: str) -> str:
        # Count the occurrences of the chars
        charCount = {}
        for c in s:
            if c in charCount:
                charCount[c] += 1
            else:
                charCount[c] = 1

        res = ""
        # put them in order
        for c in order:
            if c in charCount:
                occurences = charCount.pop(c)
                for i in range(occurences):
                    res += c

        # append everything else in the end
        while charCount:
            c, occurences = charCount.popitem()
            for i in range(occurences):
                res += c
        
        return res