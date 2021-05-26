num = int(input("Enter the number of rows: "))
for i in range(num,0,-1):
    for j in range(0,num-i):
        print(end=" ")
    for j in range(0,i):
        print("*",end=" ")
    print()


# num = 11
# for i in range (0,num,1):
#     print(i)