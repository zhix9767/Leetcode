class Solution(object):
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if not matrix or not matrix[0]:
            return 0
        heights = [[0] * len(matrix[0]) for _ in range(len(matrix))]
        for i in range(len(matrix)):
            count = 0
            left = 0
            right = 0
            while right < len(matrix[0]) or left < right:
                if right < len(matrix[0]) and matrix[i][right] == '1':
                    count += 1
                    right += 1
                else:
                    for j in range(left, right):
                        heights[i][j] = count
                        count -= 1
                        left += 1
                    if right < len(matrix[0]):
                        heights[i][right] = 0
                        right += 1
                        left += 1
        result = 0
        for i in zip(*heights):
            result = max(result, self.largestRectangleArea(i))
        return result


    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        if len(heights) == 0:
            return 0
        
        stack = [0]
        max_area = 0
        for i in range(1, len(heights)):
            while stack and heights[i] <= heights[stack[-1]]:
                height = heights[stack.pop()]
                if stack:
                    width = i - 1 - stack[-1]
                else:
                    width = i 
                max_area = max(max_area, height * width)
            if not stack or heights[i] > heights[stack[-1]]:
                stack.append(i)
        
        while stack:
            height = heights[stack.pop()]
            if stack:
                width = len(heights) -1 - stack[-1]
            else:
                width = len(heights) 
            max_area = max(max_area, height * width)
        
        return max_area

    def maximalRectangle2(self, matrix):
        """
        :type heights: List[int]
        :rtype: int
        """
        if not matrix or not matrix[0]:
            return 0
        n = len(matrix[0])
        left = [0] * n
        right = [n] * n
        height = [0] * n
        result = 0
        for i in range(len(matrix)):
            cur_left = 0
            cur_right = n
            for j in range(n-1,-1,-1):
                if matrix[i][j] == '1':
                    right[j] = min(right[j],cur_right)
                else:
                    right[j] = n
                    cur_right = j
            for j in range(n):
                if matrix[i][j] == '1':
                    height[j] += 1
                    left[j] = max(left[j],cur_left)
                else:
                    height[j] = 0
                    left[j] = 0
                    cur_left = j + 1
                result = max(result, (right[j]-left[j])*height[j])
        return result

    def maximalRectangle3(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if not matrix or not matrix[0]:
            return 0
        n = len(matrix[0])
        height = [0] * (n + 1)
        ans = 0
        for row in matrix:
            for i in range(n):
                height[i] = height[i] + 1 if row[i] == '1' else 0
            stack = [-1]
            for i in range(n + 1):
                while height[i] < height[stack[-1]]:
                    h = height[stack.pop()]
                    w = i - stack[-1] - 1
                    ans = max(ans, h * w) 
                stack.append(i) 
        return ans