matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(matrix[0][1]) # returns 2
print(matrix[0][2]) # returns 3

matrix[0][1] = 20
print(matrix[0][1]) # returns 20

for row in matrix:
    for item in row:
        print(item) # returns 1, 20, 3, 4, 5, 6, 7, 8, 9