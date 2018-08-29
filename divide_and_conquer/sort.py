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

def main():
    _ = int(input())
    arr = list(map(int, input().split()))
    sortings = Sortings(arr)
    print(sortings.recursive_merge_sort())


def test(number_of_tests):
    s = Sortings()
    t = 0
    for i in range(number_of_tests):
        for i in range(10**4):
            s.arr.append(randint(0, 10**9))
        print("Array len: {}\nmax_el: {}\n min_el: {}".format(len(s.arr), max(s.arr), min(s.arr)))
        t0 = time.perf_counter()
        s.insertion_sort()
        t1 = time.perf_counter()
        t += t1 - t0
        s.arr=[]

    print("Insertion sort speed on 10^5 {}".format(t / number_of_tests))

if __name__ == "__main__":
    main()

