class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        freq1 = {}
        freq2 = {}

        len_s1 = len(s1)

        for i in range(len_s1):
            freq1[s1[i]] = freq1.get(s1[i], 0) + 1
        
        left = 0
        right = 0

        while right < len(s2):

            

            freq2[s2[right]] = freq2.get(s2[right], 0) + 1
            right += 1

            if right - left > len_s1:                
                left_char_freq = freq2[s2[left]] - 1

                if left_char_freq == 0:
                    freq2.pop(s2[left])
                else:
                    freq2[s2[left]] = left_char_freq
                
                left += 1

            if freq1 == freq2:
                return True

        return False