# Given an m x n grid of characters board and a string word, return true if word exists in the grid.

# The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.

# Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
# Output: true

# Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE"
# Output: true

# Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB"
# Output: false

def word_search(board, word):
    row, col =  len(board), len(board[0])

    def dfs(r, c, i):
        if i == len(word):
            return True
        
        if r >= row or c >= col or board[r][c] != word[i] or board[r][c] == "#":
            return False
        
        temp = board[r][c]
        board[r][c] = "#"
        res = (dfs(r+1, c, i+1) or
               dfs(r-1, c, i+1) or
               dfs(r, c+1, i+1) or
               dfs(r, c-1, i+1)
            )
        
        board[r][c] = temp
 
        return res
    
    for r in range(row):
        for c in range(col):
            if board[r][c] == word[0] and dfs(r, c, 0):
                return True
            

    return False

print(word_search([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "ABCCED") == True)
print(word_search([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "SEE") == True)
print(word_search([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "ABCB") == False)