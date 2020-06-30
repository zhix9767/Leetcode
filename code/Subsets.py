class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if not nums:
            return []
        if len(nums) == 1:
            return [[nums],[]]
        result = [[]]
        for i in nums:
            for k in list(result):
                result.append(k+[i])
        return result

