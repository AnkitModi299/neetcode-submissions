class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res , sol = [] , []
        n = len(s)
        def backtrack(i,j):
            if i>= len(s):
                if i == j:
                    res.append(sol.copy())
                return
            if self.isPalindrome(s,j,i):
                sol.append(s[j:i+1])
                backtrack(i+1, i+1)
                sol.pop()        
            backtrack(i+1, j)

        backtrack(0,0)
        return res

    def isPalindrome(self, s, l, r):
        while l<r:
            if s[l] != s[r]:
                return False
            l,r = l+1,r-1
        return True                