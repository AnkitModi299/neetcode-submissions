class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t)> len(s):
            return ""
        dict1={}
        dict2={}
        for i in t:
            dict1[i] = 1+dict1.get(i,0)
        correct = 0
        req = len(dict1)    
 
        l=0
        reslen = float("inf")
        fl = 0
        
        mincount = len(s)
        for r in range(len(s)):
            dict2[s[r]] = 1 + dict2.get(s[r],0)
            
            if s[r] in dict1 and dict2[s[r]] == dict1[s[r]]: 
                correct +=1

            while correct == req:
                if (r-l+1) < reslen: 
                    reslen = r-l+1
                    fl = l
                dict2[s[l]] -=1
                if s[l] in dict1 and dict2[s[l]] < dict1[s[l]]:
                    correct -=1    
                l+=1

        return s[fl:fl+reslen] if reslen != float("inf") else "" 

      