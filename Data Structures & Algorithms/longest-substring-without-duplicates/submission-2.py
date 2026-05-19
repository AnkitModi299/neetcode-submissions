class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxcount = 0
        set1 = set()
        l = 0
        for r in range(len(s)):
            while s[r] in set1:
                set1.remove(s[l])
                l+=1
            set1.add(s[r])
            maxcount = max(maxcount,r-l+1)
            
        return maxcount    