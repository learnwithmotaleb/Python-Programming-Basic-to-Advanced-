matrix = [
     [1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]
]

print("Matrix: ", matrix)

print("Matrix: ",matrix[0])
print("Matrix: ",matrix[0][2])
print("Matrix: ",matrix[2][2])

n = len(matrix)

# Diagonal Elements
print(n)
for i in range(n):
     print(matrix[i][i], end=" ")

#Upper Triangular Matrix
print("\n")
for i in range(n):
     for j in range(i, n):
          print(matrix[i][j], end= " " )


print("\nLower Triangle:")
for i in range(n):
    for j in range(i+1):
        print(matrix[i][j], end=" ")  # 1 4 5 7 8 9