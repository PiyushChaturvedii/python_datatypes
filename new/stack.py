# Stack
# Last in first out
# or
# first in last out

# base - top

# Push, Pop, Peek or top, isEmpty

# push - append
# pop- pop


# 1. list
# 2. modules

# stack = []

# stack.append(10)
# stack.append(20)
# stack.append(30)

# print (stack)

# stack.pop()
# print("After poping")
# print (stack)


# stack.pop()
# print("After poping")
# print (stack)


stack= []

def push():
    if len(stack) == n:
        print("List is full!")
    else:
        element = input("Enter the element: ")
        stack.append(element)
        print(stack)

def pop_element():
    if not stack:
        print("Stack is empty!")
    else:
        e = stack.pop()
        print("removed element: ", e)
        print(stack)

n = int(input("Limit of stack: "))
while True:
    print("Select the operation 1. push 2. pop 3. quit")
    choice = int(input())
    if choice == 1:
        push()
    elif choice == 2:
        pop_element()
    elif choice == 3:
        break
    else:
        print("Enter the correct operation!")