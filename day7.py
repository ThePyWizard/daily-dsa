#print fibonacci series using recursion

def fibonacci(n, a=0, b=1):
    if n <= 0:
        return "Invalid input. Please enter a positive integer."
    elif n == 1:
        return [a]
    else:
        return [a] + fibonacci(n - 1, b, a + b)

n_terms = int(input("enter limit :"))
result = fibonacci(n_terms)
print(f"Fibonacci series with {n_terms} terms: {result}")
