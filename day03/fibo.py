import random


# print('fibo.py:',__name__)

def fibonacci(n):
    a, b = 0, 1
    while b < n:
        print(b, end=' ')
        a, b = b, a + b
    print()


def fibonacci_recursive(n):
    if (n <= 1):
        return 1
    elif (n > 1):
        return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)


def print_fib(n):
    for i in range(n):
        print(fibonacci_recursive(i), end=" ")


if __name__ == '__main__':
    print('n이 5일 때, fibonacci')
    fibonacci(5)
