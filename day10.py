#reverse a string and check if its palindrome

x=input("enter a string:")
print("Reversed Version:",x[::-1])
if (x==x[::-1]):
    print("Its a Palindrome")
else:
    print("Its not a Palindrome")
