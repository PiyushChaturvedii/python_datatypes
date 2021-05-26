# import numpy as np
# a = np.array([[1,2],[3,4]])
# b = np.array([[10,20],[30,40]])
# c = b - a
# print(c)

# a*b
# a.dot(b)

# # *

# # dot()

# # transpose: of a matrix is an opertor which flips a matrix over its diagonal.

# np.transpose(a)
# a.transpose()

# from numpy import matrix


# row = int(input("enter the row number:"))
# col = int(input("enter the column number:"))

# print("enter the elements for matrix1:")
# matrix1 = [[int(input())for i in range(col)]for j in range(row)]
# print ("matrix1:")
# for i in range(row):
#     for j in range (col):
#         print(format(matrix1[i][j],"<5"),end="")
#     print()
# print("enter the elements for matrix2:")
# matrix2 = [[int(input())for i in range(col)]for j in range(row)]
# print ("matrix2:")
# for i in range(row):
#     for j in range (col):
#         print(format(matrix2[i][j],"<5"),end="")
#     print()

# result = [[0 for i in range(col)] for j in range(row)]
# for i in range(row):
#     for j in range (col):
#         result[i][j]=matrix1[i][j] - matrix2[i][j]

# print("result is : ")
# for i in range(row):
#     for j in range(col):
#         print(format(result[i][j],"<5"),end="")
#     print()


# **************************multiplication*****************************

# No. of column in matrix1 == No. of rows in matrix2

        # p X n               ==                  nXq

        # result = pXq


# 1. Number of rows in matrix1 (P)
# 2. number of rows in matrix2 or number of column in matrix1 (N)
# 3. Number of column in matrix2 (q)


p = int(input("enter the row number:"))
q = int(input("enter the column number:"))
n = int(input("enter the column number for matrix1/ row number of matrix2: "))

print("enter the elements for matrix1:")
matrix1 = [[int(input())for i in range(n)]for j in range(p)]
print ("matrix1:")
for i in range(p):
    for j in range (n):
        print(format(matrix1[i][j],"<5"),end="")
    print()
print("enter the elements for matrix2:")
matrix2 = [[int(input())for i in range(q)]for j in range(n)]
print ("matrix2:")
for i in range(n):
    for j in range (q):
        print(format(matrix2[i][j],"<5"),end="")
    print()

result = [[0 for i in range(q)] for j in range(p)]
for i in range(p):
    for j in range (q):
        for k in range (n):
            result[i][j]=result[i][j]+matrix1[i][k] * matrix2[k][j]

print("result is : ")
for i in range(p):
    for j in range(q):
        print(format(result[i][j],"<5"),end="")
    print()
