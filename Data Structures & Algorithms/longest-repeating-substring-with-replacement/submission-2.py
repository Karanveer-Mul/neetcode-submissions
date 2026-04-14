class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq = {}

        left = 0

        longest_string = 0
        max_cont_freq = 0

        for right, ch in enumerate(s):
            freq[ch] = freq.get(ch, 0) + 1

            max_cont_freq = max(max_cont_freq, freq[ch])

            while (right - left + 1) - max_cont_freq > k:
                freq[s[left]] -= 1
                left += 1

            longest_string = max(longest_string, right - left + 1)

        return longest_string