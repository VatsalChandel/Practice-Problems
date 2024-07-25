def zeroMatrix(matrix):
    n,m = len(matrix), len(matrix[0])
    
    row = set()
    cols = set()
    
    for i in range(n):
        for j in range(m):
            if matrix[i][j] == 0:
                row.add(i)
                cols.add(j)
    
    for i in row:
        for j in range(m):
            matrix[i][j] = 0
    
    for j in cols:
        for i in range(n):
            matrix[i][j] = 0 

matrix = [
    [1, 2, 3],
    [4, 0, 6],
    [7, 8, 9]
]

zeroMatrix(matrix)

for row in matrix:
    print(row)