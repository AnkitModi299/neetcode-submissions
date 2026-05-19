class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = [] # time, posn
        for i in range(len(position)):
            time = (target - position[i]) / speed[i]
            stack.append((time,position[i]))
        
        sorted_stack = stack.sort(key=lambda x: x[1])
        s1 = []
        fleet = len(position)

        for i in range(len(stack)):
            while s1 and stack[i][0]>= s1[-1]:
                s1.pop()
                fleet-=1
            s1.append(stack[i][0])
        return fleet        