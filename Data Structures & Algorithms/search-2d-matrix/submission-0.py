class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        max_hor_len = len(matrix[0])
        max_ver_len = len(matrix)

        # First find the row

        top = 0
        bottom = max_ver_len - 1
        mid = 0

        while top <= bottom:

            mid = top + (bottom - top)//2

            if target >= matrix[mid][0] and target <= matrix[mid][max_hor_len - 1]:
                break
            elif target < matrix[mid][0]:
                bottom = mid - 1
            elif target > matrix[mid][max_hor_len - 1]:
                top = mid + 1
        
        # Second find the element in row
        left = 0
        right = max_hor_len - 1
        row = mid

        while left <= right:
            mid = left +  (right - left)//2

            if target == matrix[row][mid]:
                return True
            elif target > matrix[row][mid]:
                left = mid + 1
            else:
                right = mid -1
        
        return False

