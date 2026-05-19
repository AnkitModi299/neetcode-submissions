class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        i = 0
        while i< len(nums):
            diff = target - nums[i]
            if diff in nums and nums.index(diff) != i:
                j = nums.index(diff) 
                return [i,j] if i<j else [j,i]
            i+=1

    