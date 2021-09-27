import time
from time import *
import math


# f(x) = a[0] + a[1]x + a[2]x^2 + ... + a[n-1]x^(n-1) + a[n]x^n
def f(n, x):
    a = [1000000,1,2,2,3,3,4,4,5,5]
    p = a[0]
    for i in range(0, n):
        if i <= n:
            p += a[i] * math.pow(x, i)
    return p


def f2(n,x):
    a = [1000000, 1, 2, 2, 3, 3, 4, 4, 5, 5]
    p = a[0]
    for i in range(0, n):
        p = a[i-1] + x * p
    return p


if __name__ == '__main__':
    start_time = time()
    f(10, 2)
    stop_time = time()
    timer = stop_time - start_time
    print(start_time)
    print(stop_time)
    print(timer)
    print()

    start_time2 = time()
    f2(10, 2)
    stop_time2 = time()
    timer2 = stop_time2 - start_time2
    print(start_time2)
    print(stop_time2)
    print(timer2)
    print(timer > timer2)
