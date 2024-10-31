def fibonacci(n):
    if not isinstance(n, int) or n < 0:
        raise ValueError("Input must be a non-negative integer")
    if n <= 1 :
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

# Test cases
print(fibonacci(0))  # Expected: 0
print(fibonacci(5))  # Expected: 5
print(fibonacci(10)) # Expected: 55
