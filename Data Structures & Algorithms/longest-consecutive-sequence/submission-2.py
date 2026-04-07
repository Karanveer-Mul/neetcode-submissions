class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if (len(nums) <= 1): return len(nums)

        sortedArr = sorted(nums)
        maxLen = 1
        cur = 1

        for i in range(1, len(nums)):
            if (sortedArr[i] - 1 == sortedArr[i-1]):
                cur += 1
            elif (sortedArr[i] == sortedArr[i-1]):
                continue
            else:
                cur = 1
            
            maxLen = max(cur, maxLen)

        return maxLen