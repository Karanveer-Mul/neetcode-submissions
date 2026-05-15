class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        word_dict = {}


        for s in strs:
            key = "".join(sorted(s))

            if key not in word_dict:
                word_dict[key] = []
            word_dict[key].append(s)
        
        result = []

        for key, value in word_dict.items():
            result.append(value)


        return result