class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = 0
        stack = []

        for i, height in enumerate(heights):
            # The potential start index for the current height because we have not 
            # checked if it's less than the previous heights yet
            start = i

            # If there is a value in the stack and the height is greater than the current height
            # pop the previous height because it cannot be extended further, calculate the area 
            # for that bar then set the starting index of the current bar back to the bar that 
            # was popped(it can be extended backwards)
            while stack and stack[-1][1] > height:
                index, prev_height = stack.pop()
                maxArea = max(maxArea, prev_height * (i - index))
                start = index
            stack.append((start, height))


        for i, height in stack:
            maxArea = max(maxArea, height * (len(heights) - i))

        return maxArea