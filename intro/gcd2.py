def gcd(a, b):
    return gcd(b, a % b) if b else a

def main():
    a, b = map(int, input().split())
    print(gcd(a, b))

if __name__ == "__main__":
    main()
