class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        # since n queens and n rows and n colums, each queen will occupy a row
        # so if we place one queen on a row we can eliminate that row similarly a column
        # we call method for every starting osition of the first row
        # now how do we handle with the diagonal
        # when we place a queen we can mark all r+1,c+1; r-1,c-1; r-1,c+1; r+1,c-1. positions as a dot while they are within ranges n,n. Similarly we can do for that row r,c-1 and r,c+1 and column r-1,c and r+1,c

        # now while placing a queen, our main fn goes through rows so we return false if that box has a dot and iterate to the next column in that row

        res = []
        board = [["."] * n for i in range(n)]


        cols = set()
        diag1 = set()
        diag2 = set()

        def backtrack(i):
            if i==n:
                copy = ["".join(row) for row in board]
                res.append(copy)
                return
            for m in range(n):
                if m in cols or (i+m) in diag1 or (i-m) in diag2:
                    continue
                
                cols.add(m)
                diag1.add(i+m)
                diag2.add(i-m)
                board[i][m] = "Q"
                backtrack(i+1)

                cols.remove(m)
                diag1.remove(i+m)
                diag2.remove(i-m)
                board[i][m] = "."


        backtrack(0)
        return res        