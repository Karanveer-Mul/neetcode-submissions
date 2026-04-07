class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        target_dict = {}

        for i,num in enumerate(nums):

            if num not in target_dict:
                target_dict[target - num] = i
            else:
                return [target_dict[num], i]