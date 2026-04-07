class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        arr_len = len(nums)
        result = [1] * arr_len

        product_without_zero = 1
        zero_count = 0

        for i in range(arr_len):
            if nums[i] != 0:
                product_without_zero *= nums[i]
            else:
                zero_count += 1
        
        for i in range(arr_len):
            if nums[i] != 0:
                if zero_count > 0:
                    result[i] = 0
                    continue
                result[i] = product_without_zero//nums[i]
            else:
                if zero_count > 1:
                    result[i] = 0
                    continue
                result[i] = product_without_zero

        return result