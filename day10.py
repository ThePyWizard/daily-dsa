#reverse a string and check if its palindrome

x=input("enter a string:")
if (x==x[::-1]):
    print("Its a Palindrome")
else:
    print("Its not a Palindrome")
