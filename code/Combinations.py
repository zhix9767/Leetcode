class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        if n == 0 or k == 0:
            return []
        result = []
        nums = []
        self.helper(0, n, k, nums, result)
        return result
    
    def helper(self, left, right, k, nums, result):
        if len(nums) == k:
            result.append(list(nums))
        for i in range(left,right):
            nums.append(i+1)
            self.helper(i+1, right, k, nums, result)
            nums.pop()

    
    def combine2(self, n, k):
        ans = []
        stack = []
        x = 1
        while True:
            l = len(stack)
            if l == k:
                ans.append(stack[:])
            if l == k or x > n - k + l + 1:
                if not stack:
                    return ans
                x = stack.pop() + 1
            else:
                stack.append(x)
                x += 1