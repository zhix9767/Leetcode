class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        if not candidates:
            return []
        candidates.sort()
        result = []
        for i in range(len(candidates)):
            if candidates[i] > target:
                return result
            if candidates[i] == target:
                result.append([candidates[i]])
                return result
            next = candidates[i:len(candidates)]
            temp = self.combinationSum(next, target - candidates[i])
            if temp:
                for j in temp:
                    j.append(candidates[i])
                    result.append(j)
        return result