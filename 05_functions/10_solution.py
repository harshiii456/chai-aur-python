def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)
    
factor = factorial(4)
print(factor)  # Output: 120