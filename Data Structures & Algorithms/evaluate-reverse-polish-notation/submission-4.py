class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        todo = [] 
        for i in range(len(tokens)):
            
            if tokens[i] =='+':
                val1 = int(todo.pop())
                val2 = int(todo.pop())
                res = val1+val2
                todo.append(res)
            elif tokens[i] =='-':
                val1 = int(todo.pop())
                val2 = int(todo.pop())
                res = val2-val1
                todo.append(res)
            elif tokens[i] =='*':
                val1 = int(todo.pop())
                val2 = int(todo.pop())
                res = val1*val2
                todo.append(res)
            elif tokens[i] == '/':
                val1 = int(todo.pop())
                val2 = int(todo.pop())
                res = int(val2/val1)
                todo.append(res)
            else:
                todo.append(int(tokens[i]))
                    
        return todo.pop()


