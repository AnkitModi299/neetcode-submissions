class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res, sol = [], []
        n = len(nums)
        sum1 = 0

        def backtracking(i):
            nonlocal sum1
            if sum1 == target:
                res.append(sol[:])
                return
            if i == n or sum1 > target:
                return     
           
            # case of adding same number in nums
            sol.append(nums[i])
            sum1 = sum1 + nums[i]
            backtracking(i)
            tal = sol.pop()
            sum1 = sum1 - tal
            # case of skipping the number
            backtracking(i+1)
            
        backtracking(0)
        return res    