class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []  # pair: [temp, index]

        for i in range(len(temperatures)):
            t = temperatures[i]
            while stack and t > stack[-1][0]: # while element is greater than temp of previous days
                stackT, stackInd = stack.pop() # remove stack element
                res[stackInd] = i - stackInd # update that o/p index with difference in days
            stack.append((t, i)) # add new element
        return res
