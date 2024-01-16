#find the nth fibonacci series number

x=int(input("Enter nth term for the fibonacci series: "))
def f(n):
    if n==1:
        return 1
    elif n==2:
        return 1
    else:
        return f(n-1)+f(n-2)
print(f(x))
