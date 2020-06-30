class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        left = 0
        right = len(nums) - 1
        for i in range(len(nums)):
            while nums[i] == 0 or nums[i] == 2:
                if nums[i] == 0:
                    if i <= left:
                        break
                    nums[i], nums[left] = nums[left], nums[i]
                    left += 1
                else:
                    if i >= right:
                        break
                    nums[i], nums[right] = nums[right], nums[i]
                    right -= 1
        return