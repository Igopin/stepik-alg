#!/usr/bin/python3
import sys
from random import randint

class Sortings:
    def __init__(self, arr=[], value=lambda x: x):
        self.arr = arr
        self.value = value

    def swap_by_ind(self, i, j):
        self.arr[i], self.arr[j] = self.arr[j], self.arr[i]

    def partition(self, begin, end):
        less = begin
        for i in range(less + 1, end + 1):
            if self.value(self.arr[i]) < self.value(self.arr[begin]):
                less += 1; self.swap_by_ind(less, i)

        self.swap_by_ind(begin, less)

        same = less
        for i in range(same + 1, end + 1):
            if self.value(self.arr[i]) == self.value(self.arr[same]):
                same += 1; self.swap_by_ind(i, same)

        return less - 1, same + 1

    def __quick_sort(self, begin, end):
        if (begin >= end):
            return
        self.swap_by_ind(begin, randint(begin, end))
        left_pivot, right_pivot = self.partition(begin, end)

        self.__quick_sort(begin, left_pivot)
        self.__quick_sort(right_pivot, end)

    def quick_sort(self):
        self.__quick_sort(0, len(self.arr) - 1)
        return self.arr


class Search:
    def __init__(self, arr, value=lambda x: x):
        self.arr = arr
        self.value = value

    def binary_search(self, key, find_first=True):
        last = len(self.arr) - 1
        if self.value(self.arr[0]) > key:
            res = 0
        elif self.value(self.arr[last]) < key:
            res = last
        else:
            res = self.__bin_s_first(key) if find_first else self.__bin_s_last(key)
        return res

    def __bin_s_first(self, key):
        left, right = 0, len(self.arr) - 1

        while left <= right:
            mid_ind = (left + right) // 2
            mid = self.value(self.arr[mid_ind])

            if (mid == key):
                res = mid_ind
                if mid_ind > 0:
                    right = mid_ind - 1
                else:
                    break
            elif (mid > key):
                right = mid_ind - 1
            else:
                left = mid_ind + 1
        else:
            lval = self.value(self.arr[left])
            rval = self.value(self.arr[right])
            res = left if (lval - key) < (key - rval) else right
        return res

    def __bin_s_last(self, key):
        left, right = 0, len(self.arr) - 1

        while left <= right:
            mid_ind = (left + right) // 2
            mid = self.value(self.arr[mid_ind])

            if (mid == key):
                res = mid_ind
                if mid_ind + 1 < len(self.arr):
                    left = mid_ind + 1
                else:
                    break
            elif (mid > key):
                right = mid_ind - 1
            else:
                left = mid_ind + 1
        else:
            lval = self.value(self.arr[left])
            rval = self.value(self.arr[right])
            res = left if (lval - key) < (key - rval) else right
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


def calculate(segments_begins, segments_ends, points):
    segments_count = []

    size = len(segments_begins)

    Sortings(segments_begins).quick_sort()
    Sortings(segments_ends).quick_sort()

    bsearch= Search(segments_begins)
    esearch = Search(segments_ends)

    for p in points:
        l_first = bsearch.binary_search(p)
        if l_first == 0 and p < segments_begins[l_first]:
            segments_count.append(0)
            continue

        r = esearch.binary_search(p)
        if r == size - 1 and p > segments_ends[r]:
            segments_count.append(0)
            continue

        l_last = bsearch.binary_search(p, False)

        summary = l_first if p < segments_begins[l_first] else l_last + 1
        summary -= r if p <= segments_ends[r] else r + 1

        segments_count.append(summary)
    return segments_count


def main():
    reader = file_reader(sys.stdin)
    n, m = next(reader)

    segments_begins, segments_ends = [], []
    for _ in range(n):
        begin, end = next(reader)
        segments_begins.append(begin); segments_ends.append(end)
    points = list(next(reader))

    print(" ".join(str(el) for el in calculate(segments_begins, segments_ends, points)))


if __name__ == "__main__":
    main()

