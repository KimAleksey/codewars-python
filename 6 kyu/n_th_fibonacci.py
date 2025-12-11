"""
https://www.codewars.com/kata/522551eee9abb932420004a0
"""

def nth_fib(n):
    # if n < 3:
    #     return n - 1
    # return nth_fib(n-2) + nth_fib(n-1)

    f = [0, 1]
    if n < 3:
        return f[n-1]
    for i in range(2, n):
        f.append(f[i-1] + f[i-2])
    return f[-1]

print(nth_fib(7))