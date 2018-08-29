#!/usr/bin/python3

inversions = 0

def merge(left, right):
    res = []
    ll, lr = len(left), len(right)
    il, ir = 0, 0

    while il < ll and ir < lr:
        if left[il] < right[ir]:
            res.append(left[il]); il += 1
        else:
            res.append(right[ir]); ir += 1
            inversions += lr - ir - 1

    while il < ll:
        res.append(left[il]); il += 1
    while ir < lr:
        res.append(right[ir]); ir += 1

    return res

def merge_sort(arr, begin, end):
    if begin < end:
        mid = (begin + end) // 2
        return merge(merge_sort(arr, begin, mid), merge_sort(arr, mid + 1, end))
    return [arr[begin]]

def sort(arr):
    return merge_sort(arr, 0, len(arr) - 1)

def insertion_sort(arr):
    for i in range(1, len(arr)):
        cur = i
        while cur > 0 and arr[cur] < arr[cur - 1]:
            arr[cur], arr[cur - 1] = arr[cur - 1], arr[cur]; cur -= 1
    return arr

def main():
    _ = int(input())
    arr = list(map(int, input().split()))
    sort(arr)
    print(inversions)

if __name__ == "__main__":
    main()

