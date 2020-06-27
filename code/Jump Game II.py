class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return 0
        maxReach = [0] * len(nums)
        maxReach[0] = nums[0]
        count = 1
        reach = nums[0]
        for i in range(len(nums)):
            if i > reach:
                reach = maxReach[count]
                count += 1
            maxReach[count] = max(maxReach[count], nums[i]+i)
        for i in range(len(maxReach)):
            if maxReach[i] >= len(nums) - 1:
                return i + 1
