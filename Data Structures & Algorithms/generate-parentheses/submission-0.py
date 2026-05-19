class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def recurse(openP,closedP,s):
            if openP == closedP and openP+closedP == 2*n:
                res.append(s)
                return
            if openP < n:
                recurse(openP+1,closedP,s+"(")

            if closedP< openP:
                recurse(openP,closedP+1,s+")")   
        recurse(0,0,"")             
        return res    