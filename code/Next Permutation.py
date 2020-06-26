class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        if len(nums) == 0 or len(nums) == 1:
            return
        for i in range(len(nums)-1, 0, -1):
            if nums[i] > nums[i-1]:
                for j in range(len(nums)-1, i-1, -1):
                    if nums[j] > nums[i-1]:
                        nums[i-1] = nums[i-1] ^ nums[j]
                        nums[j] = nums[i-1] ^ nums[j]
                        nums[i-1] = nums[i-1] ^ nums[j]
                        break;
                nums[i:len(nums)] = sorted(nums[i:len(nums)])
                return
        nums.reverse()
        return
                        