def fibonacci_number(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci_number(n-1) + fibonacci_number(n-2)

def print_fibonacci_sequence(n):
    if n <= 0:
        return
    print(fibonacci_number(n), end=", ")
    print_fibonacci_sequence(n-1)

print_fibonacci_sequence(10)