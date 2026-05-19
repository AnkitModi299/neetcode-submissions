class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) == 1 or nums[0] < nums[-1]:
            return nums[0]
        l=1
        r=len(nums)-1
        res = float("inf")
        while l<=r:
            if nums[l] <= nums[r]:
                return nums[l]
            l+=1    
