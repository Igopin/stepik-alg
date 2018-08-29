#!/usr/bin/python3
import sys

class BinarySearch:
    def __init__(self, arr):
        self.arr = arr

    def search(self, key):
        res = -1
        left, right = 0, len(self.arr) - 1
        while left <= right:
            mid_ind = (left + right) // 2
            mid = self.arr[mid_ind]

            if (mid == key):
                res = mid_ind
                break
            elif (mid > key):
                right = mid_ind - 1
            else:
                left = mid_ind + 1
        return res

def split_line_on_ints(reader):
    def inner(file_to_read):
        for line in reader(file_to_read):
            yield map(int, line.split())
    return inner

@split_line_on_ints
def file_reader(file_to_read):
    for line in file_to_read:
        yield line

def main():
    reader = file_reader(sys.stdin)
    _, *array = next(reader)
    _, *keys = next(reader)

    res = []
    b = BinarySearch(array)
    for key in keys:
        res.append(b.search(key))
    print(" ".join(map(str, res)))

if __name__ == "__main__":
    main()

