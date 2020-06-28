class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return -float('inf')
        if len(nums) == 1:
            return nums[0]
        start = 0
        end = len(nums) - 1
        middle = (start + end) // 2
        maxLeft, maxRight, leftSum, rightSum = 0, 0, 0, 0
        for i in range(middle-1, -1, -1):
            leftSum += nums[i]
            maxLeft = max(maxLeft, leftSum)
        for i in range(middle+1, len(nums)):
            rightSum += nums[i]
            maxRight = max(maxRight, rightSum)
        return max(self.maxSubArray(nums[0:middle]),self.maxSubArray(nums[middle+1:len(nums)]),maxLeft+maxRight+nums[middle])