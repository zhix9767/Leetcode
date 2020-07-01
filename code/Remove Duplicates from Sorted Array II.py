class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        left = 0
        right = 0
        res = 0
        checkNum = nums[0]
        count = 0
        while right < len(nums):
            if checkNum == nums[right]:
                count += 1
            else:
                checkNum, count = nums[right], 1
            if count > 2:
                right += 1
            else:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right += 1
                res += 1
        return res
    