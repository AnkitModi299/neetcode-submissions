class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()
        maxcount = 1
        count = 1
        if len(nums) == 0:
            return 0
        for i in range(len(nums)):
            if i == 0 or nums[i] == nums[i-1]:
                continue
            if nums[i] != nums[i-1]+1:
                if count > maxcount:
                    maxcount = count
                count = 1    
                continue
            count+=1
        return maxcount if maxcount>count else count    