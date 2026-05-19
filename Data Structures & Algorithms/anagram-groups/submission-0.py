class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict1 = {}
        for i in strs:
            key = tuple(sorted(i))
            if key in dict1:
                dict1[key].append(i)
            else: 
                dict1[key] = [i]
        
        return list(dict1.values())            