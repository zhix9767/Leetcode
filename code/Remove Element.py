class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        pointer1 = 0
        pointer2 = len(nums) - 1
        while pointer1 <= pointer2:
            if nums[pointer1] == val:
                nums[pointer1],nums[pointer2] = nums[pointer2],nums[pointer1]
                pointer2 -= 1
            else:
                pointer1 += 1
        return pointer1
            