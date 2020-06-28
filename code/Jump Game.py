class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        reach, i = 0, 0
        lens = len(nums)
        while i < lens - 1 and i <= reach:
            reach = max(reach, i + nums[i])
            i += 1
        return reach >= len(nums) - 1