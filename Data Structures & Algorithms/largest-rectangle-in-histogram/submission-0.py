class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        
        n  = len(heights)
        stack = []

        left = [-1] * n

        for i in range(n):
            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()
            if stack:
                left[i] = stack[-1]
            
            stack.append(i)
        
        right = [n] * n
        stack = []
        for i in range(n-1, -1, -1):
            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()
            if stack:
                right[i] = stack[-1]
            stack.append(i)
        maxArea = 0

        for i in range(n):
            # Get just after left smaller element
            left[i] += 1
            # Get just before right smaller element
            right[i] -= 1

            length = right[i] - left[i] + 1 # Because subtraction gives you the distance between indices, not the count.
            maxArea = max(maxArea,  length * heights[i])

        return maxArea