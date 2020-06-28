class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        self.permute2(nums, 0, result)
        return result

    def permute2(self, nums, i, result):
        if i == len(nums):
            result.append(list(nums))
            return
        for j in range(i, len(nums)):
            nums[i], nums[j] = nums[j], nums[i]
            self.permute2(nums, i+1, result)
            nums[i], nums[j] = nums[j], nums[i]