#implement a python code to perform stack operations on an array

array = []
top = 0

def push():
    ele = int(input("Enter element: "))
    array.append(ele)

def pop():
    global top
    if top != 0:
        array.pop()  
        top -= 1  

def display():
    length = len(array)
    if length == 0:
        print("Stack is empty")
    else:
        for i in range(length - 1, -1, -1):
            print(array[i])

while True:
    print("1. to push")
    print("2. to pop")
    print("3. to display")
    print("4. to exit")
    opt = int(input("Choose option: "))
    if opt == 1:
        top += 1
        push()
    elif opt == 2:
        pop()
    elif opt == 3:
        display()
    elif opt == 4:
        break
    else:
        print("Invalid option")
