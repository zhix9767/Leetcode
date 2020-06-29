class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        stack = []
        path = path.split('/')
        for i in path:
            if not i or i == '.':
                continue
            elif i == '..':
                if stack:
                    stack.pop()
                else:
                    continue
            else:
                stack.append(i)
        result = ''
        for i in stack:
            result += ('/' + i)
        return '/'+'/'.join(stack)
        