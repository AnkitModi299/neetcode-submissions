class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # at each step take the min cost of getting upto that stair.
        n = len(cost)
        DP = [0] * (n+1)
        DP[0] = cost[0]
        DP[1] = cost[1]
        
        for i in range(2,n+1):
            if i == n:
                DP[i] = min(DP[i-1], DP[i-2])
                return DP[n]  
            DP[i] = cost[i] + min(DP[i-1], DP[i-2])
        return DP[n+1]    