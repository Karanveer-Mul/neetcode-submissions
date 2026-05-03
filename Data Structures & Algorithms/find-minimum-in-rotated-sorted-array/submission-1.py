class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        left = 0
        right = len(nums) - 1

        mid = left + (right - left)//2

        #Check if rotatedd array

        if nums[left] < nums[right]:
            return nums[left]

        if right == 0:
            return nums[0]

        while left <= right: 

            mid = left + (right - left)//2

            if nums[mid - 1] > nums[mid]:
                return nums[mid]
            if nums[mid] > nums[mid + 1]:
                return nums[mid+1]

            if nums[mid] > nums[left] :
                left = mid + 1
            elif nums[mid] <= nums[right] :
                right = mid - 1

        return nums[left]