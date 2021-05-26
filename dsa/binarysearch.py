# Binary Search
# 1. Findout the middle element in the sorted list
# 2. Compare"key" with the middle element
# 3. if "key" matches with middle element, print message "key is found". STOP.
# 4. else if key is greater that the middle element, then "key" is searched in right sublist. start with the step 1.
# 5. else if "key " is smaller than the middle element "key" searched in left sublist. start with step 1.
# 6. else print key is not found


def Binarysearch(list1,key):
    low = 0
    high = len(list1)-1
    Found = False
    while low<= high and not Found:
        mid = (low + high)//2
        if key == list1[mid]:
            Found = True
        elif key > list1[mid]:
            low = mid+1
        else:
            high = mid-1
    
    if Found == True:
        print("key is Found")
    else:
        print("key is not Found")
list1= [23,1,4,2,3]
# num = int(input("enter the list lenght: "))
# list1 = [int(input()) for i in range(num)]
list1.sort()
print(list1)
key = int(input("enter the key: "))
Binarysearch(list1,key)


