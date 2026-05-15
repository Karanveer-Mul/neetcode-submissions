class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix = [1] * n
        sufix = [1] * n
        
        for i in range(1, n):
            prefix[i] = prefix[i-1] * nums[i-1]
            sufix[n - i - 1] = sufix[n - i] * nums[n - i] 

        result = [0] * n

        for i in range(n):
            result[i] = prefix[i] * sufix[i]

        return result