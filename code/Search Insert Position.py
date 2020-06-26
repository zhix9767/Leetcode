class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums:
            return 0
        left = 0
        right = len(nums) - 1
        while left < right:
            middle = (left + right + 1) // 2
            if nums[middle] > target:
                right = middle - 1
            else:
                left = middle
        if nums[left] >= target:
            return left
        else:
            return left + 1