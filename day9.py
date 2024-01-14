#implement queue using the arrays

array = []
while True:
    print("1. add element")
    print("2. remove element")
    print("3. display queue")
    print("4. exit")
    op = int(input("enter your option: "))
    if op == 1:
        ele = int(input("enter element: "))
        array.append(ele)
    elif op == 2:
        if len(array) > 0:
            removed_element = array.pop(0)
            print(f"Removed element: {removed_element}")
        else:
            print("Queue is empty.")
    elif op == 3:
        print(array)
    elif op == 4:
        break
    else:
        print("Invalid option. Please enter a valid option.")
