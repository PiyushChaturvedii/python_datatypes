# Selection Sort Algorithm: in-place Comparison based algorithm
# Algorithm:
# 1. Starting from the first element search for smallest (biggest) element in the list of numbers.
# 2. Swap  minimum(maximum) number with first element.
# 3. take the sublist(ignore sorted part) and repeat step 1 and 2 until all the elements are sorted.


num = int(input("how many numbers you want to enter? : "))
list1 = [int(input("enter number: ")) for x in range(num)]
print("unsorted list : ",list1)

for i in range (len(list1)-1):
    # min_val = min(list1[i:])
    min_val = list1[i]
    for j in range(i+1,len(list1)):
        if list1[j] > min_val:
            min_val = list1[j]
    min_ind = list1.index(min_val,i)
    if list1[i] != list1[min_ind]:
        list1[i], list1[min_ind] = list1[min_ind], list1[i]
    
    print(list1)




# for i in range (len(list1)):
#     min_val = min(list1[i:])
#     min_ind = list1.index(min_val)
#     list1[i], list1[min_ind] = list1[min_ind], list1[i]
#     print(list1)
