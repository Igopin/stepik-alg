def fib_mod(n, m):
    period = [0, 1]

    a, b = 0, 1
    for _ in range(6*m):
        a, b = b, (a + b) % m
        period.append(b);
        if a == 0 and b == 1:
            break

    period = period[:-2]
    return period[n % len(period)]


def main():
    n, m = map(int, input().split())
    print(fib_mod(n, m))

if __name__ == "__main__":
    main()
