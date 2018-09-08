#!/usr/bin/python3

def count_sort(arr):
    counts = [0 for _ in range(10)]

    for el in arr:
        counts[el - 1] += 1

    i = 0
    for k, el in enumerate(counts):
        for j in range(el):
            arr[i] = k + 1; i += 1
    return arr

def main():
    _ = input()
    arr = list(map(int, input().split()))
    print(" ".join(str(e) for e in count_sort(arr)))

if __name__ == "__main__":
    main()
