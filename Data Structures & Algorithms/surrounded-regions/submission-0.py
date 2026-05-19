class Solution:
    def solve(self, board: List[List[str]]) -> None:
        m, n = len(board), len(board[0])
        border = deque()
        for r in range(m):
            if board[r][0] == "O":
                border.append((r,0))
            if board[r][n-1] == "O":
                border.append((r,n-1))
        for c in range(n):
            if board[0][c] == "O":
                border.append((0,c))        
            if board[m-1][c] == "O":
                border.append((m-1,c)) 
        dirn = [[1,0],[-1,0],[0,1],[0,-1]]
        

        def bfs(r,c,border):
            while border:
                r,c = border.popleft()
                if board[r][c] == "O":
                    board[r][c] = "W"
                for dr,dc in dirn:
                    nr = r+dr
                    nc = c+dc
                    if 0<=nr<m and 0<=nc<n and board[nr][nc] == "O":
                        border.append((nr,nc))
                        
        bfs(r,c,border)
        for r in range(m):
            for c in range(n):
                if board[r][c] == "O":
                    board[r][c] = "X"
                if board[r][c] == "W":
                    board[r][c] = "O"


