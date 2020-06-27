class Solution(object):
    def combinationSum2(self, candidates, target):
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
            if i > 0 and candidates[i] == candidates[i-1]:
                continue
            if candidates[i] > target:
                return result
            if candidates[i] == target:
                result.append([candidates[i]])
                return result
            next = candidates[i+1:len(candidates)]
            temp = self.combinationSum2(next, target - candidates[i])
            if temp:
                for j in temp:
                    j.append(candidates[i])
                    result.append(j)
        return result
