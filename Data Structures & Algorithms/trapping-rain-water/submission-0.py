class Solution:
    def trap(self, height: List[int]) -> int:
        lenArr = len(height)
        left = [0] * lenArr 
        right = [0] * lenArr

        trappedWater = 0
        prevMaxHeight = 0

        for i in range(lenArr):
            prevMaxHeight = max(prevMaxHeight, height[i])
            left[i] = prevMaxHeight - height[i]

        prevMaxHeight = 0

        for i in range(lenArr - 1, -1, -1):
            prevMaxHeight = max(prevMaxHeight, height[i])
            right[i] = prevMaxHeight - height[i]

        for i in range(lenArr):
            trappedWater += min(left[i], right[i])

        return trappedWater