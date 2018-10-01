#!/usr/bin/python

def pack(capacity, weights):
    curr_row = [0 for i in range(capacity + 1)]
    prev_row = curr_row[:]

    for i, w in enumerate(weights):
        for curr_cap in range(1, capacity + 1):
            curr_row[curr_cap] = prev_row[curr_cap]
            if curr_cap >= w:
                curr_row[curr_cap] = max(prev_row[curr_cap], prev_row[curr_cap - w] + w)
        prev_row = curr_row[:]
    return curr_row[capacity]


def main():
    capacity, _ = map(int, input().split())
    w = list(map(int, input().split()))
    print(pack(capacity, w))

if __name__ == "__main__":
    main()

