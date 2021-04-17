# Linear Search:
# 1. Start from the Leftmost element of list and one by one compare
# "key"
# with each element of the list.
# 2. if "key" matches with an element, return True.
# 3. else return False.

def search(list1, key):
    list2=[]
    flag = False
    for i in range (len(list1)):
        if key == list1[i]:
            flag = True
            list2.append(i)

    if flag == True:
        print("Key elemnt is found at index: ")
        for i in list2:
            print(i)
    else:
        print("element is not found")


list1 = [10,20,20,30,40,50]
print(list1)
# num = int(input("list length: "))
# list1 = [int (input()) for i in range(num)]
key = int(input("Enter the key element: "))
search(list1,key)

