class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        mapping = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', 
                   '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}

        if len(digits) == 0:
            return ""
        elif len(digits) == 1:
            return [i for i in mapping[digits[0]]]
        else:
            part1 = [i for i in mapping[digits[0]]]
            part2 = self.letterCombinations(digits[1:])
            return [i + j for i in part1 for j in part2]
