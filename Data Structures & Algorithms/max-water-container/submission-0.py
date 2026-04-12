class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        left = 0
        right = len(heights) - 1

        area = 0

        while left < right:

            l_h = heights[left]
            r_h = heights[right]

            area = max(area,(right - left) * min(l_h, r_h))

            if (l_h < r_h):
                left += 1
            else:
                right -= 1

        return area


