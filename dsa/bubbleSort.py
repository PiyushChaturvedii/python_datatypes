# Bubble sorted
# refferred as sinking sort
# simple sorting algorithm which sorts n number of elements in the list by comparing the wach pair of
# items and swaps them if they are in wrong order.

# Algorithm:
# 1. Starting with the first element(index=0) compare the current element with the next element of the list.
# 2. If the current element is greater than the next element of the list swap them.
# 3. if the current element is less than the next element, move to the next element. Repeat step 1.

list1 = []
num = int(input("input the range of list: ") )
print("enter value: ")
for k in range(num):
    list1.append(int(input()))

print("unsorted list: ", list1)

for j in range(len(list1)-1,0,-1):
    for i in range(j):
        if list1[i] > list1[i+1]:
            list1[i], list1[i+1] = list1[i+1], list1[i]
        #     print(list1)
        # else:
        #     print(list1)
        # print()

print("sorted list: ", list1)
