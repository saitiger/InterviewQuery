# Solution 1 
def matrix_sum(matrix):
    row = len(matrix)
    columns = len(matrix[0])

    s = 0 
    for r in range(rows):
        for c in range(columns):
            s+=matrix[r][c]
    
    return s 

# Solution 2 
def matrix_sum(matrix):
    return sum(sum(row) for row in matrix)
