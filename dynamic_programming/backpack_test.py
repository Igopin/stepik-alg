#!/usr/bin/python

def pack(capacity, weights):
    prev_row = [0 for i in range(weights)]

    current, prev = 0, 0
    for i in len(weights):
        for c in range(capacity):
            current = prev
            if weights[i] <= c:
                current = max()




def main():
    capacity, _ = map(int, input().split())
    w = list(map(int, input().split()))
    print(pack(capacity, w))

if __name__ == "__main__":
    main()

