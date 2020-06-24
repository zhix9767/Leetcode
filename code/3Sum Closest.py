class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        nums.sort()
        result = nums[0] + nums[1] +nums[2]
        for i in range(len(nums)):
            j = i + 1
            k = len(nums) - 1
            while j < k:
                if abs(result-target) > abs(nums[i]+nums[j]+nums[k]-target):
                    result = nums[i]+nums[j]+nums[k]
                if nums[i]+nums[j]+nums[k] > target:
                    k -= 1
                elif nums[i]+nums[j]+nums[k] < target:
                    j += 1
                else:
                    return target
        return result
