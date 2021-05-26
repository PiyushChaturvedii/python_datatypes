# 1. Python program can return 1 or More number of values

# def foo():
#     a = 10
#     b = 20
#     return a,b

# x,y = foo()
# print(x,y)

# 2. Python allows negative indexing

# mylist = ['apple','snow','ball']
# print(mylist[2])
# print(mylist[-2])

# 3. Combining Multiple Strings.

# mylist=['Shan','kumar','sharma']
# print(' '.join(mylist))

# 4. Swapping is a pieace of cake.
# x = 10
# y = 20
# print('Before swapping ',x,y,"\n")
# x,y = y,x
# print('After swapping ', x, y, "\n")

# Know your Python version
# import sys
# print('Python version is ', sys.version)

# Store all values of list in new separate variables.

# mylist = [1,2,3,4]
# print('list is ',mylist)
# p,q,r,s= mylist
# print('p is', p)
# print('q is', q)
# print('r is', r)
# print('s is', s)

# covert nested list into one list.
# list_of_lists = [[1,2],[3,4],[5,6]]
# flattened_list = [y for x in list_of_lists for y in x]
# print(flattened_list)

# Simple way to Transpose a Matrix
# import numpy as np
# matrix=[[1,2,3],[4,5,6]]
# print(np.transpose(matrix))

# Unconventional way to describe a function : Lambda
# subtract = lambda a, b : a-b
# print(subtract(100,59))

# Slice assignmnet Operator 
# list1 = ['p','i','n','g','u']
# list2 = [1,2,3,4,5,6,7]

# Append list1 in list2
# list2[:0] = list1

# list2[:2] = list1

# Replace all
# list2[:] = list1
# print(list2)


# string = "Pingu"
# result = []
# result[:]= string
# print(result)

# remove Null from LIST
# list = [1, None, 2, None, 3]
# print("Orignal list is ", list)

# result = []
# for i in list:
#     if(i is not None):
#         result.append(i)


# print("New list without none is \n ", result)

# Iterate with enumerate() instead of range(len())
# data = [1,2,-4,-3]
# for i in range(len(data)):
#     if data[i] < 0:
#         data[i]=0

# print(data)

# data = [1,2,-4,-3]
# for idx, num in enumerate(data):
#     if num<0:
#         data[idx]= 0

# print(data)


# use List Compreshensions instead of for raw loops
# squares = []
# for i in range(10):
#     squares.append(i*i)

# print(squares)

# squares = [i*i for i in range(10)]
# print(squares)

# Sort complex iterables with sorted()

# data = (3,5,1,10,9)
# sorted_data = sorted(data, reverse = True)
# print(sorted_data)

# data = [
#     {"name":"Max", "age":3},
#     {"name":"Ben", "age":9},
#     {"name":"Lisa", "age":6},
# ]

# sorted_data = sorted(data, key= lambda x: x["age"])

# print(sorted_data)

# Store unique values with Sets
# my_list = [1,2,3,4,4,4,5,5,5,6,6,6,7,7,7]
# my_set = set(my_list)
# print(my_set)

# Save Memory with Generators
# import sys
# my_list = [i for i in range(10000)]
# print(sum(my_list))
# print(sys.getsizeof(my_list),"bytes")

# my_gen = (i for i in range(10000))
# print(sum(my_gen))
# print(sys.getsizeof(my_gen),"bytes")

# define default values in Dictionaries with .get() and .setdefault()

# my_dict = {"item":"football","price":10.00}
# count = my_dict.get("count", 0)
# print(count)

# count = my_dict.setdefault("count",0)
# print(count)
# print(my_dict)

from collections import Counter


# Count hashable objects with collections.counter

my_list=[10,10,10,5,5,5,5,5,2,9,9,9,9,9,9]
counter = Counter(my_list)
most_common = counter.most_common(2)
counter.
print(most_common)
print(counter[20])
