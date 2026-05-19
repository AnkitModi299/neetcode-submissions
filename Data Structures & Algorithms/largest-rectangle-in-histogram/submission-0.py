class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        stack1 = [-1]*n
        stack2 = [n]*n
        stack= []
        for i in range(len(heights)):
            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()
            if stack:
                stack1[i] = stack[-1]     
            stack.append(i)
            
        stack = []
        for i in range(n - 1, -1, -1):
            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()
            if stack:
                stack2[i] = stack[-1]
            stack.append(i)

        maxA = 0
        for i in range(n):
            stack1[i] +=1
            stack2[i] -=1
            maxA = max(maxA, heights[i]*(stack2[i]-stack1[i]+1))
        return maxA    
