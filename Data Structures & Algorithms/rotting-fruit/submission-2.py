class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # its a bfs question, we find min distance for each fresh fruit to a rotten fruit and we find the max of these mins
        q = collections.deque()
        m,n = len(grid), len(grid[0])
        seen = set()
        fresh = 0
        time = 0

        for r in range(m):
            for c in range(n):
                if grid[r][c] == 1: # keeping count of total fresh apples
                    fresh += 1
                if grid[r][c] == 2: # adding rotten apple to queue
                    q.append((r, c))

        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        while fresh>0 and q:
            length = len(q)
            for i in range(length):
                r,c = q.popleft()
                for dr,dc in directions:
                    row,col = r+dr,c+dc
                    if row>=0 and row<m and col>=0 and col<n and grid[row][col] == 1:
                        grid[row][col] = 2
                        q.append((row,col))
                        fresh-=1
            time+=1
        return time if fresh == 0 else -1                

                    
