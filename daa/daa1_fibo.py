import timeit

def fibonacci(n):
    """Non recursive fibonacci function"""
    for i in range(2, n + 1):
        fib_list[i] = fib_list[i - 1] + fib_list[i - 2]
    return fib_list[n]

def fibonacci_recursive(n):
    """Recursive fibonacci function"""
    if n == 0:
        return 0
    if n == 1:
        return 1
    fib_recur_list[n] = fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)
    return fib_recur_list[n]

RUNS = 1000

while True:
    print("Menu:")
    print("1. Calculate Fibonacci (Non-Recursive)")
    print("2. Calculate Fibonacci (Recursive)")
    print("3. Quit")
    choice = input("Enter your choice (1/2/3): ")
    if choice == '1':
        N = int(input("Enter the value of N: "))
        fib_list = [0] * (N + 1)
        fib_list[0] = 0
        fib_list[1] = 1
        result = fibonacci(N)
        time_taken = timeit.timeit("fibonacci(N)", setup="from __main__ import fibonacci, N", number=RUNS)
        print(f"Fibonacci({N}) = {result}")
        print(f"Time: {time_taken:.6f} seconds (O(n)), Space: O(1)\n")
    elif choice == '2':
        N = int(input("Enter the value of N: "))
        fib_recur_list = [0] * (N + 1)
        fib_recur_list[0] = 0
        fib_recur_list[1] = 1
        result = fibonacci_recursive(N)
        time_taken = timeit.timeit("fibonacci_recursive(N)", setup="from __main__ import fibonacci_recursive, N", number=RUNS)
        print(f"Fibonacci({N}) = {result}")
        print(f"Time: {time_taken:.6f} seconds (O(2^n)), Space: O(n)\n")
    elif choice == '3':
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please select a valid option.")
