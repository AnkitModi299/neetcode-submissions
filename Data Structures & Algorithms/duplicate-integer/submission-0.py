class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # we need O(n) runtime use for loop and if condition inside
        dict1 = {}
        for i in nums:
            if i in dict1:
                return True
            else:
                dict1[i] = 1
        return False        
