class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 0:
            return 0
        maxLength = 0
        stack = []
        stack.append(-1)
        for i in range(len(s)):
            if s[i] == '(':
                stack.append(i)
            else:
                j = stack.pop()
                if not stack:
                    stack.append(i)
                else:
                    maxLength = max(maxLength, i - stack[-1])
        return maxLength


    def longestValidParentheses2(self, s):
        if len(s) == 0:
            return 0
        dp = [0] * len(s)
        for i in range(1,len(s)):
            if s[i] == '(':
                dp[i] == 0
            else:
                if dp[i-1] == '(':
                    dp[i] = (dp[i-2] if i > 2 else 0) + 2
                elif i-dp[i-1]>0 and s[i-dp[i-1]-1] == '(':
                    dp[i] = dp[i-1] + (dp[i-dp[i-1]-2] if i-dp[i-1]-2 >= 0 else 0) + 2
        return max(dp)

    def longestValidParentheses3(self, s):
        if len(s) == 0:
            return 0
        left = 0
        right = 0
        maxLength = 0
        for i in range(len(s)):
            if s[i] == '(':
                left += 1
            else:
                right += 1
                if right == left:
                    maxLength = max(maxLength, 2 * left)
                elif right > left:
                    left, right = 0, 0
        left = 0
        right = 0
        for i in range(len(s)-1, -1, -1):
            if s[i] == ')':
                right += 1
            else:
                left += 1
                if left == right:
                    maxLength = max(maxLength, 2* left)
                elif left > right:
                    left, right = 0, 0
        return maxLength
                    