# Given an m x n matrix, return all elements of the matrix in spiral order.

# Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
# Output: [1,2,3,6,9,8,7,4,5]

# Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
# Output: [1,2,3,4,8,12,11,10,9,5,6,7]

def spiral_matrix(matrix):
    row, col = len(matrix), len(matrix[0])
    res = []

    def traverse(matrix, r, c):
        if r >= row or c >= col or matrix[r][c] == "#":
            return
        
        res.append(matrix[r][c]) 
        matrix[r][c] = "#"

        if c + 1 > r: 
            traverse(matrix, r, c+1)
        traverse(matrix, r+1, c)
        traverse(matrix, r, c-1)
        traverse(matrix, r-1, c)

    
    traverse(matrix, 0, 0)
    return res

print(spiral_matrix([[1,2,3],[4,5,6],[7,8,9]])== [1,2,3,6,9,8,7,4,5])
print(spiral_matrix([[1,2,3,4],[5,6,7,8],[9,10,11,12]]) == [1,2,3,4,8,12,11,10,9,5,6,7])
        
