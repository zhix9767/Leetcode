class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        result = []
        self.permute2(nums, 0, result)
        return result

    def permute2(self, nums, i, result):
        if i == len(nums) and nums not in result:
            result.append(list(nums))
            return
        for j in range(i, len(nums)):
            nums[i], nums[j] = nums[j], nums[i]
            self.permute2(nums, i+1, result)
            nums[i], nums[j] = nums[j], nums[i]

    def permuteUnique2(self, nums):
        ans = [[]]
        for n in nums:
            new_ans = []
            for l in ans:
                for i in range(len(l)+1):
                    new_ans.append(l[:i]+[n]+l[i:])
                    if i<len(l) and l[i]==n:
                         break
            ans = new_ans
        return ans