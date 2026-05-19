class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        dict1 = {}
        for i in nums:
            dict1[i] = 1+ dict1.get(i,0)
            if dict1[i] > 1:
                return i
                