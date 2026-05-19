class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        pre = [0]*n
        post = [0]*n
        val = [0]*n
        pre[0] = height[0]
        post[n-1]=height[n-1]
        
        for i in range(1,n-1):
            pre[i] = max(height[i],pre[i-1])
        for i in range(n-2,0,-1):
            post[i]= max(height[i], post[i+1])
        for i in range(len(height)):
            val[i] = min(pre[i],post[i])-height[i]
            if val[i]<0:
                val[i] = 0
        return sum(val)    

