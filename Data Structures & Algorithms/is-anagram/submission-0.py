class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if (len(s) != len(t)):
            return False

        s_dict = {}
        t_dict = {}

        for i in range(len(s)):
            c = s[i] 
            if c in s_dict:
                s_dict[c] += 1
            else:
                s_dict[c] = 1      
            
            c = t[i]
            if c in t_dict:
                t_dict[c] += 1
            else:
                t_dict[c] = 1   

        for key in t_dict.keys():
            if (key not in s_dict):
                return False

            if (t_dict[key] != s_dict[key]):
                return False

        return True