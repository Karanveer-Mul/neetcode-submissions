class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        for i, num in enumerate(nums):
            if i>0 and nums[i-1] == num:
                continue

            left = i+1
            right = len(nums) - 1

            while left<right:
                numSum = num + nums[left] + nums[right]

                if numSum > 0:
                    right -= 1
                elif numSum < 0:
                    left += 1
                else:
                    result.append([num, nums[left], nums[right]])
                    left += 1
                    while left < right and nums[left] == nums[left-1]:
                        left += 1

        return result
