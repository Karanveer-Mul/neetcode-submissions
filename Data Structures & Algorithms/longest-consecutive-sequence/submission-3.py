class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        if len(nums)< 1:
            return 0

        sorted_arr = sorted(nums)

        long_seq = 1
        cur_seq = 1
        for i in range(1, len(sorted_arr)):
            if (sorted_arr[i] == sorted_arr[i-1]):
                continue
            elif(sorted_arr[i] == (sorted_arr[i-1] + 1)):
                cur_seq += 1
                long_seq = max(long_seq, cur_seq)
            else:
                cur_seq = 1
        
        return long_seq

        