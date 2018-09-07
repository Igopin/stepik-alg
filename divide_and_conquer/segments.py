#!/usr/bin/python3
import sys
from random import randint

class Sortings:
    def __init__(self, arr=[]):
        self.arr = arr

    def swap_by_ind(self, i, j):
        self.arr[i], self.arr[j] = self.arr[j], self.arr[i]

    def partition(self, begin, end):
        less = equal = begin
        for i in range(less + 1, end + 1):
            if self.arr[i] < self.arr[begin]:
                less += 1; self.swap_by_ind(less, i); equal += 1;
                if less != equal:
                    self.swap_by_ind(i, equal)
            elif self.arr[i] == self.arr[begin]:
                equal += 1; self.swap_by_ind(equal, i)

        self.swap_by_ind(begin, less)

        return less - 1, equal + 1

    def __quick_sort_elim(self, begin, end):
        while begin < end:
            self.swap_by_ind(begin, randint(begin, end))
            left_pivot, right_pivot = self.partition(begin, end)

            self.__quick_sort_elim(begin, left_pivot)
            begin = right_pivot

    def quick_sort(self):
        self.__quick_sort_elim(0, len(self.arr) - 1)
        return self.arr


class Search:
    def __init__(self, arr):
        self.arr = arr

    def binary_search(self, key, find_first=True):
        last = len(self.arr) - 1
        if self.arr[0] > key:
            res = 0
        elif self.arr[last] < key:
            res = last
        else:
            res = self.__bin_s_first(key) if find_first else self.__bin_s_last(key)
        return res

    def __bin_s_first(self, key):
        left, right = 0, len(self.arr) - 1

        while left <= right:
            mid_ind = (left + right) // 2
            mid = self.arr[mid_ind]

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
            lval = self.arr[left]
            rval = self.arr[right]
            res = left if (lval - key) < (key - rval) else right
        return res

    def __bin_s_last(self, key):
        left, right = 0, len(self.arr) - 1

        while left <= right:
            mid_ind = (left + right) // 2
            mid = self.arr[mid_ind]

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
            lval = self.arr[left]
            rval = self.arr[right]
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

    bsearch = Search(Sortings(segments_begins).quick_sort())
    esearch = Search(Sortings(segments_ends).quick_sort())

    for p in points:
        l_first = bsearch.binary_search(p)
        r = esearch.binary_search(p)

        if p < segments_begins[l_first]:
            summary = l_first
        else:
            l_last = bsearch.binary_search(p, False)
            summary = l_last + 1
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

