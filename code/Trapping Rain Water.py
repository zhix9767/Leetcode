class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if not height:
            return 0
        left, right, result = 0, len(height)-1, 0
        while left < right:
            if height[left] < height[right]:
                temp = left
                while height[left] <= height[temp]:
                    result += height[temp] - height[left]
                    left += 1
            else:
                temp = right
                while height[right] <= height[temp] and left < right:
                    result += height[temp] - height[right]
                    right -= 1
        return result