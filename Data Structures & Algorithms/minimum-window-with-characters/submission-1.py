class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        if t == "":
            return ""

        if s == t:
            return t

        left = 0
        window = {}
        target_freq = {}

        min_len = float('inf')
        min_left = 0

        for i in range(len(t)):
             target_freq[t[i]] = target_freq.get(t[i], 0) + 1

        required = len(target_freq)
        formed = 0

        for right in range(len(s)):

            char = s[right]
            window[char] = window.get(char, 0) + 1

            if char in target_freq and window[char] == target_freq[char]:
                formed += 1

            while left <= right and formed == required:

                if right - left + 1 < min_len:
                    min_len = right - left + 1
                    min_left = left

                left_char = s[left]
                window[left_char] = window.get(left_char, 0) - 1

                if left_char in target_freq and window[left_char] < target_freq[left_char]:
                    formed -= 1
                
                left += 1

        if min_len != float('inf'):
            return s[min_left:min_left + min_len]

        return ""
