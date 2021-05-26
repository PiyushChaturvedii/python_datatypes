import numpy as np
a = np.array([[1,2],[3,4]])
b = np.array([[10,20],[30,40]])
c =a + b
print(c)
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