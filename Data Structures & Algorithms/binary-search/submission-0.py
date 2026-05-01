class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        left = 0
        right = len(nums) - 1

        while left <= right:

            half = left + (right - left)//2

            if target == nums[half]:
                return half

            if nums[half] > target:
                right = half - 1
            else:
                left =  half + 1
        
        return -1
