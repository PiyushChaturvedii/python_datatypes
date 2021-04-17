# Binary Search:
# 1. Findout the middle element in the sorted list.
# 2. Compare "key" with the middle element.
# 3. if "key" matches with middle element, print message "key is found". STOP
# 4. else if key is greater than the middle element, the "key" is searched in right sublist. start with the step 1.
#
#     fourmula to find mid:
#             mid = low+high/2
#
# main rule of binary search:
# key == list1[mid]   fail
# key  > list1[mid]   fail
# key < list1[mid]   fail
#
# no element is found

def BinarySearch(list1,key):
    low = 0
    high = len(list1) -1
    flag = False

    while low<=high and not flag:
        mid = (low+high)//2

        if key == list1[mid]:
            flag = True
        elif key >list1[mid]:
            low = mid +1
        else: high = mid -1
    if flag == True:
        print ("key is found")
    else:
        print("key is not found")

list1 = [23,1,4,2,3]
list1.sort()
print(list1)
key = int(input("enter the key: "))
BinarySearch (list1, key)