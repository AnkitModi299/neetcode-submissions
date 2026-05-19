class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res, sol = [], []
        n = len(candidates)
        candidates.sort()

        def backtrack(i,sol,total):
            if total == target:
                res.append(sol.copy())
                return
            if total > target or i == n:
                return

            sol.append(candidates[i])
            backtrack(i+1,sol,total + candidates[i])
            sol.pop()

            while i+1< n and candidates[i] == candidates[i+1]:
                i+=1
            backtrack(i+1, sol, total)
        backtrack(0, sol, 0)
        return res    

        
        