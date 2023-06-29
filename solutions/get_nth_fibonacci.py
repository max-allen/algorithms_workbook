# Given an integer n, return the nth number of the Fibonacci sequence
# (https://en.wikipedia.org/wiki/Fibonacci_sequence).

# the first two numbers in the sequence are 0, and 1. subsequent numbers
# are derived from the sum of the two previous (n-1 + n-2).

# 3 -> 2 (0 + 1)

# 6 -> 5 (2 + 3)

# NOTE: Solve recursively.


def get_nth_fibonacci(n, fib_hash={1: 0, 2: 1}):
    if n in fib_hash:
        return fib_hash[n]
    else:
        fib_hash[n] = get_nth_fibonacci(n - 1, fib_hash) + get_nth_fibonacci(
            n - 2, fib_hash
        )
        return fib_hash[n]
