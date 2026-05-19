class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dict1 = {}
        for i in nums:
            if i in dict1:
                dict1[i]+=1
            else:
                dict1[i] = 1
        r=0
        keys = [0]*k
        while r<k:
            keys[r] = max(dict1, key = dict1.get)
            del dict1[keys[r]]
            r+=1   
        return keys
