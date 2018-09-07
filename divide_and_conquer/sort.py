#!/usr/bin/python3
import sys
from random import randint
import time

class Sortings:
    def __init__(self, arr=[]):
        self.arr = arr

    def merge_sort(self):
        pass

    def __merge(self, left, right):
        res = []
        ll, lr = len(left), len(right)
        il, ir = 0, 0

        while il < ll and ir < lr:
            if left[il] < right[ir]:
                res.append(left[il]); il += 1
            else:
                res.append(right[ir]); ir += 1

        while il < ll:
            res.append(left[il]); il += 1

        while ir < lr:
            res.append(right[ir]); ir += 1

        return res

    def __recursive_merge_sort(self, begin, end):
        if begin < end:
            mid = (begin + end) // 2
            return self.__merge(self.__recursive_merge_sort(begin, mid), self.__recursive_merge_sort(mid + 1, end))
        return [self.arr[begin]]

    def recursive_merge_sort(self):
        return self.__recursive_merge_sort(0, len(self.arr) - 1)

    def insertion_sort(self):
        # copy array to leave original array untouched (just because)
        arr = self.arr
        for i in range(1, len(arr)):
            cur = i
            while cur > 0 and arr[cur] < arr[cur - 1]:
                arr[cur], arr[cur - 1] = arr[cur - 1], arr[cur]; cur -= 1
        return arr

    def swap_by_ind(self, i, j):
        self.arr[i], self.arr[j] = self.arr[j], self.arr[i]

    def partition(self, begin, end):
        less = begin
        for i in range(less + 1, end + 1):
            if self.arr[i] <= self.arr[begin]:
                less += 1; self.swap_by_ind(less, i)

        self.swap_by_ind(begin, less)
        return less

    def __quick_sort(self, begin, end):
        if (begin >= end):
            return
        self.swap_by_ind(begin, randint(begin, end))
        pivot = self.partition(begin, end)

        self.__quick_sort(begin, pivot - 1)
        self.__quick_sort(pivot + 1, end)

    def quick_sort(self):
        arr = self.arr[:]
        self.__quick_sort(0, len(self.arr) - 1)
        self.arr, arr = arr, self.arr[:]
        return arr

def main():
    arr = list(map(int, input().split()))
    s = Sortings(arr)
    print(s.quick_sort())
    print(s.arr)


def test(number_of_tests):
    s = Sortings()
    t = 0
    for i in range(number_of_tests):
        for i in range(10**8):
            s.arr.append(randint(0, 10**9))
        print("Array len: {}\nmax_el: {}\n min_el: {}".format(len(s.arr), max(s.arr), min(s.arr)))
        t0 = time.perf_counter()
        s.quick_sort()
        t1 = time.perf_counter()
        t += t1 - t0
        s.arr=[]

    print("sort speed on 10^5 {}".format(t / number_of_tests))

if __name__ == "__main__":
    main()
    #test(1)

