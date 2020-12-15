# StackS:

# Last in first out or first in last out

# plate4 - top Last & First
# plate3
# plate2
# plate1 - base first in last out

# push, pop, peek or top, isEmpty

# print("This is a write area. nothing is important here.")
#
# 1. list     - Push-append, pop-pop
# 2. module
#
# stack = []
# stack.append(10)
# stack.append(20)
# stack.append(30)
# stack.pop()
# stack.pop()
# stack.pop()



# print(stack[-1])             want to use top value
# print(len(stack)==0)      Find stack empty or not



stack=[]
def push():
    if len(stack) == n:
        print("Stack is full!")
    else:
        element = input("Enter the element: ")
        stack.append(element)
        print(stack)

def pop_element():
    if not stack:
        print("stack is empty!!")
    else:
        e = stack.pop()
        print("removed element: ", e)
        print(stack)

n = int(input("limit of stack: "))                  #limit of stack

while True:
    print("Select the operation 1. push 2. pop 3. quit")
    choice= int(input())
    if choice == 1:
        push()
    elif choice == 2:
        pop_element()
    elif choice== 3:
        break
    else:
        print("Enter the correct operation!")
