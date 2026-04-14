class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = set()
        left = 0
        right = 0

        str_len = len(s)
        ss_len = 0

        if len(s) < 2: return str_len

        while right<str_len:
            if s[right] not in charSet:
                charSet.add(s[right])
                right += 1
            else:
                charSet.remove(s[left])
                left += 1
            ss_len = max(ss_len, right - left)

        return ss_len