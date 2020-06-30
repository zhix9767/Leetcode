class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix or not matrix[0]:
            return False
        up = 0
        down = len(matrix)
        l = len(matrix[0])
        middle = 0
        while up < down:
            middle = (up + down) // 2
            if matrix[middle][0] > target:
                down = middle
            elif matrix[middle][l-1] < target:
                up = middle + 1
            else:
                break
        left = 0
        right = l
        middle2 = 0
        while left < right:
            middle2 = (left + right) // 2
            if matrix[middle][middle2] > target:
                right = middle2
            elif matrix[middle][middle2] < target:
                left = middle2 + 1
            else:
                return True
        return matrix[middle][middle2] == target

    def searchMatrix2(self, matrix, target):
        if not matrix or target is None:
            return False

        rows, cols = len(matrix), len(matrix[0])
        low, high = 0, rows * cols - 1
        
        while low <= high:
            mid = (low + high) / 2
            num = matrix[mid / cols][mid % cols]

            if num == target:
                return True
            elif num < target:
                low = mid + 1
            else:
                high = mid - 1
        
        return False