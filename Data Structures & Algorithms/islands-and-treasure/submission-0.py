class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        m , n = len(grid) , len(grid[0])
        q = collections.deque()
        landLeft = 0
        time = 1
        INF = 2**31 - 1
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 0:
                    q.append((r,c))
                if grid[r][c] >0:
                    landLeft+=1

        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        while q and landLeft>0:
            length = len(q)
            for i in range(length):
                r,c = q.popleft() 
                for dr,dc in directions:
                    row,col = r+dr, c+dc
                    if row>=0 and col>=0 and row<m and col<n and grid[row][col] == INF:
                        grid[row][col] = time
                        landLeft-=1
                        q.append((row,col))
            time+=1
        

                
                 