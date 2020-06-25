class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        pre_value = nums[0]
        pre_index = 1
        for i in range(len(nums)):
            if nums[i] > pre_value:
                nums[pre_index] = nums[i]
                pre_index += 1
                pre_value = nums[i]
        return pre_index

        