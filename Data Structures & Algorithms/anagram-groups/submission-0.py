class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        dict_col = {}

        for s in strs:
            s_dict = {}
            for i in range(len(s)):
                if s[i] not in s_dict:
                    s_dict[i] = 1
                else:
                    s_dict[i] += 1
            sorted_s = ''.join(sorted(s))
            if sorted_s not in dict_col:
                dict_col[sorted_s] = [s]
            else:
                dict_col[sorted_s].append(s)

        result = []

        for key, value in dict_col.items():
            result.append(value)

        return result