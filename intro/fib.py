def fib(n):
    if n < 2: return n

    a, b, s  = 0, 1, 0
    for i in range(n - 1):
        s = a + b
        a, b = b, s
    return s


def main():
    n = int(input())
    print(fib(n))

if __name__ == "__main__":
    main()
