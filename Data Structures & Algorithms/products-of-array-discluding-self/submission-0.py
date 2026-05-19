class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        out = [0] * len(nums)
        list1 = [0] * len(nums)
        list2 = [0] * len(nums)

        list1[0] = list2[n-1] = 1

        for i in range(1,n):
            list1[i] = nums[i - 1] * list1[i - 1]
        for i in range(n - 2, -1, -1):
            list2[i] = nums[i + 1] * list2[i + 1]
        for i in range(n):
            out[i] = list1[i] * list2[i] 
        return out




