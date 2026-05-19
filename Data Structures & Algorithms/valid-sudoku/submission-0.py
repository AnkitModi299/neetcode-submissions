class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        for row in range(9):
            seen = {}
            for col in range(9):
                val = board[row][col]
                if val != ".":
                    seen[val] = seen.get(val, 0) + 1
                    if seen[val] > 1:
                        return False

        for col in range(9):
            seen = {}
            for row in range(9):
                val = board[row][col]
                if val != ".":
                    seen[val] = seen.get(val, 0) + 1
                    if seen[val] > 1:
                        return False                
                    
        for row in range(0,8,3):
            for col in range(0,8,3):
                seen = {}
                for i in range(3):
                    for j in range(3):
                        val = board[row+i][col+j]
                        if val != ".":
                            seen[val] = seen.get(val, 0) + 1
                            if seen[val] > 1:
                                return False

        return True
        

