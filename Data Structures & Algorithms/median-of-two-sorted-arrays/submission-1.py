class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        left = 0
        m, n = len(nums1), len(nums2)
        right = m
        total = len(nums1) + len(nums2)
        half = (total)//2

        while left <= right:
            mid = left + (right - left)//2

            partition1 = mid
            partition2 = half - mid

            left1 = nums1[partition1 - 1] if partition1 > 0 else float('-inf')
            right1 = nums1[partition1] if partition1 < m else float('inf')

            left2 = nums2[partition2 - 1] if partition2 > 0 else float('-inf')
            right2 = nums2[partition2] if partition2 < n else float('inf')

            if right2 >= left1 and right1 >= left2:
                if total % 2 == 1:
                    return min(right1, right2)
                else:
                    return (max(left1, left2) + min(right1, right2))/2
            else:
                if right1 < left2:
                    left = partition1 + 1
                else:
                    right = partition1 - 1


                
           








