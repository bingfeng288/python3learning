

def print_n(n):
    if n:
        print_n(n-1)
        print(n)
    return


def print_n2(n):
    for i in range(1, n+1):
        if i <= n:
            i + 1
        print(i)
    return


def f(x):
    if x > 0:
        # return x + f(x - 1)
        f(x - 1)
        print(x)
        print(f"这是第次{x}打印")
    else:
        return 0


if __name__ == '__main__':
    # print_n(100)
    # print(f(100))
    # f(10)
    print_n2(10000)

