def last_fib(n):
    if n < 2: return n

    a, b = 0, 1
    for i in range(n - 1):
        a, b = b, (a + b) % 10
    return b


def main():
    n = int(input())
    print(last_fib(n))

if __name__ == "__main__":
    main()
