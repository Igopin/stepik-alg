#!/usr/bin/python

def pack(capacity, weights):
    prev_row = [0 for i in range(weights + 1)]

    current, prev = 0, 0
    for i, w in enumerate(weights):
        for current_cap in range(capacity):
            current = prev_row[current_cap]
            if current_cap >= w:
                current = max(current, prev_row[current_cap - w] + weights[i])
                prev_row[w - weights[i]], prev = prev, current




def main():
    capacity, _ = map(int, input().split())
    w = list(map(int, input().split()))
    print(pack(capacity, w))

if __name__ == "__main__":
    main()

