class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if not nums:
            return [-1, -1]
        left, right = 0, len(nums) - 1
        while left <= right:
            middle = (left + right) // 2
            if nums[middle] < target:
                left = middle + 1
            elif nums[middle] > target:
                right = middle - 1
            else:
                start = left
                end = right
                temp = middle
                while nums[start] != target:
                    middle1 = (temp + start) // 2
                    if nums[middle1] < target:
                        start = middle1 + 1
                    else:
                        temp = middle1
                temp = middle
                while nums[end] != target:
                    middle2 = (temp + end + 1) // 2
                    if nums[middle2] > target:
                        end = middle2 - 1
                    else:
                        temp = middle2
                return [start, end]
        return [-1, -1]
