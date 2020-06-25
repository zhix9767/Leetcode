class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        
        if len(nums) < 4:
            return []
        nums.sort()
        result = []
        for i in range(0,len(nums)-3):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            for j in range(i+1,len(nums)-2):
                if j > i+1 and nums[j] == nums[j-1]:
                    continue
                m = j + 1
                n = len(nums) - 1
                while m < n:
                    value = nums[i] + nums[j] + nums[m] + nums[n]
                    if value < target:
                        m += 1
                    elif value > target:
                        n -= 1
                    else:
                        result.append([nums[i],nums[j],nums[m],nums[n]])
                        m += 1
                        while m < n and nums[m] == nums[m-1]:
                            m += 1
        return result
