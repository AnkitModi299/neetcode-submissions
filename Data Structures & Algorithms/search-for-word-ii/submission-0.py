class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False
        self.val = None

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()
        # Insert
        for word in words:
            cur = root
            for i in word:
                if i not in cur.children:
                    cur.children[i] = TrieNode()
                cur = cur.children[i]    
            cur.endOfWord = True
            cur.val = word
            

        rows = len(board)
        cols = len(board[0])
        sol = set()
        
        def backtrack(r,c,node):   
            if r<0 or c<0 or r>= rows or c>= cols:
                return 
            char = board[r][c]
            if char == "#" or char not in node.children:
                return 
            
            next1 = node.children[char]
            if next1.endOfWord:
                sol.add(next1.val)

            board[r][c] = "#"
            backtrack(r+1, c, next1) 
            backtrack(r-1, c, next1) 
            backtrack(r, c+1, next1) 
            backtrack(r, c-1, next1)
            board[r][c] = char
            

        for r in range(rows):
            for c in range(cols):
                backtrack(r,c,root)
                    
        return list(sol)    