class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        left = 0
        right = len(s) - 1

        if right - left < 1:
            return True        
        
        lower = s.lower()
        while left < right:
            r_char = lower[right]

            if not r_char.isalnum() or r_char == ' ':
                right -= 1
                continue
            
            l_char = lower[left]

            if not l_char.isalnum() or l_char == ' ':
                left += 1
                continue
            
            if l_char != r_char:
                return False

            left += 1
            right -= 1
        
        return True

