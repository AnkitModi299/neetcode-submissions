class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxvol = 0
        l,r = 0, len(heights) - 1
        while l<r:
            vol = (r-l) * min(heights[r],heights[l])
            if vol>maxvol:
                maxvol = vol
            if heights[r]>heights[l]:
                l+=1
            else:
                r-=1
        return maxvol        
        