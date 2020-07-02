class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        
        if not heights:
            return 0
        middle = len(heights) // 2
        left = middle
        right = middle
        area = heights[middle]
        min_height = heights[middle]
        length = 1
        while left > 0 or right < len(heights)-1:
            length += 1
            if left <= 0:
                right += 1
                min_height = min(min_height, heights[right])
            elif right >= len(heights)-1:
                left -= 1
                min_height = min(min_height, heights[left])
            else:
                if heights[left-1] < heights[right+1]:
                    right += 1
                    min_height = min(min_height, heights[right])
                else:
                    left -= 1
                    min_height = min(min_height, heights[left])
            area = max(area, min_height * length)
        return max(area, self.largestRectangleArea(heights[0:middle]),self.largestRectangleArea(heights[middle+1:len(heights)]))

    def largestRectangleArea2(self, heights):
        n = len(heights)

        left = [1] * n
        right = [1] * n
        area = 0

        for i in range(0, n):
            j = i - 1
            while j >= 0:
                if heights[j] >= heights[i]:
                    left[i] += left[j]
                    j -= left[j]
                else: break

        for i in range(n - 1, -1, -1):
            j = i + 1
            while j < n:
                if heights[j] >= heights[i]:
                    right[i] += right[j]
                    j += right[j]
                else: break

        for i in range(0, n):
            area = max(area, heights[i] * (left[i] + right[i] - 1))

        return area

    def largestRectangleArea3(self, heights):
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