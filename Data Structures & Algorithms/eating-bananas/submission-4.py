class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        k = float("inf")
        r = max(piles)
        l = 1
        while l <= r:  # iterating thru all possible k values
            mid = (l + r)//2
            count = 0
            for i in range(len(piles)):
                count += (piles[i]+mid-1)// mid

            if count > h:
                l = mid + 1
            else:
                r = mid - 1
                k = min(mid,k)
        return k   
        
                        

