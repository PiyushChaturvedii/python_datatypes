# intorduction of queue
# fifo            lilo
# operation
# enqueue
# dequeue
# isFull
# isEmpty
# List
# Modules
# enqueue: process of adding elements to queue
# dequeue: Process of removing the elements from the queue
# enqueue: append method
# dequeue: pop method
# queue = []
# queue.append(10)
# queue.append(20)
# queue.append(30)
# queue.pop(0)
# queue.pop(0)
# queue.pop(0)
# print(queue)
# queue = []
# queue.insert(0,10)
# queue.insert(0,20)
# queue.insert(0,30)
# # queue.pop()
# # queue.pop()
# # queue.pop()
# # print(not queue)
# print(queue[0])

queue=[]
def enqueue():
    element = input("Enter the element:")
    queue.append(element)
    print(element, "is added to queue!")

def dequeue():
    if not queue:
        print("queue is empty!")
    else:
        e = queue.pop(0)
        print("removed element:",e)
def display()
    print(queue)

while True:
    print("Select the operation 1. add 2.")