class Solution:
    def isValid(self, s: str) -> bool:
        dict1={}
        dict1[')'] = '('
        dict1['}'] = '{'
        dict1[']'] = '['
        stack1 = []
        for r in range(len(s)):
            if s[r] in dict1.values():
                stack1.append(s[r])
            if s[r] in dict1.keys():
                if len(stack1) ==0:
                    return False
                if stack1.pop() != dict1[s[r]]:
                    return False
        if len(stack1) !=0:
            return False
                        
        return True            
        