# Solution 1 
def reverse_rows(matrix):
    for i in range(len(matrix)): # For each row 
        start, end = 0, len(matrix[i]) - 1
        while start < end:
            # Swap the elements at start and end
            matrix[i][start], matrix[i][end] = matrix[i][end], matrix[i][start]
            start += 1
            end -= 1

# Solution 2 : Using in-built function
def reverse_rows(matrix):
    for row in matrix:
        row.reverse()
