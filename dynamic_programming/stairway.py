#!/usr/bin/python3

def max_steps(steps):
    p1, p2 = 0, 0
    for i in range(len(steps)):
        p1, p2 = p2, steps[i] + max(p1, p2)

    return p2

def main():
    _, steps = input(), list(map(int, input().split()))
    print(max_steps(steps))

if __name__ == "__main__":
    main()

