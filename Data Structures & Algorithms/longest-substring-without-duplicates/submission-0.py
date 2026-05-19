class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxCount = 0
        count = 0
        i,r = 0,0;
        list1 = []
        while r < len(s):
            if not s[r] in list1:
                list1.append(s[r])
                count+=1
                r+=1
                maxCount = max(maxCount,count)
            else:
                list1.clear()
                i+=1
                r=i
                count = 0
        return maxCount
            
        