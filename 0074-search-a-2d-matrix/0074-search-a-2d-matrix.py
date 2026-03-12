class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows, cols = len(matrix), len(matrix[0])
        left, right = 0, rows * cols - 1

        while left <= right:
            mid = (left + right) // 2
            r = mid // cols
            c = mid % cols
            curr = matrix[r][c]
    
            if curr < target:
                left = mid + 1
            elif curr > target:
                right = mid - 1
            else:
                return True
        
        return False