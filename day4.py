#write a  python code to implement a basic calculator

while True:
    x=int(input("Enter a number : "))
    y=int(input("Enter a number :"))
    op=input("select operator (+,-,*,/) : ")
    if (op=="+"):
        print("x+y=",x+y)
    elif (op=="-"):
        print("x-y=",x-y)
    elif (op=="*"):
        print("x*y=",x*y)
    elif (op=="/"):
        print("x/y=",x/y)
    else:
        print("Invalid Operator")
    ans=input("do you wanna try again (y or n):")
    if (ans=="n"):
        break
