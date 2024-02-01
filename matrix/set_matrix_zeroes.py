# Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's.

# You must do it in place.

# Input: matrix = [[1,1,1],[1,0,1],[1,1,1]]
# Output: [[1,0,1],[0,0,0],[1,0,1]]

# Input: matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
# Output: [[0,0,0,0],[0,4,5,0],[0,3,1,0]]

def set_zeros(matrix):
    rows, cols = [False for _ in range(len(matrix))], [False for _ in range(len(matrix[0]))]

    for r in range(len(matrix)):
        for c in range(len(matrix[0])):
            if matrix[r][c] == 0:
                rows[r], cols[c] = True, True

    
    for r in range(len(matrix)):
        for c in range(len(matrix[0])):
            if rows[r] or cols[c]:
                matrix[r][c] = 0 

    return matrix


# Test cases
print(set_zeros([[1,1,1],[1,0,1],[1,1,1]]) == [[1,0,1],[0,0,0],[1,0,1]])
print(set_zeros([[0,1,2,0],[3,4,5,2],[1,3,1,5]]) == [[0,0,0,0],[0,4,5,0],[0,3,1,0]])
        