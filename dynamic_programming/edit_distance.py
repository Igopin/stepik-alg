#!/usr/bin/python

def diff(a, b):
    return int(a != b)

def count_edit_distance(first, second):

    if len(first) > len(second):
        first, second = second, first

    # storing only previous row
    prev_row = [i for i in range(len(second) + 1)]

    # set current to 1 if one of strings is empty
    current, left = int(len(first) != len(second)), 0

    for i, c in enumerate(first):
        prev_row[0], left = i, i + 1
        for j, s in enumerate(second):
            current = min(left + 1, prev_row[j + 1] + 1, prev_row[j] + diff(c, s))
            prev_row[j], left = left, current
        prev_row[j + 1] = current

    return current

def main():
    first = input()
    second = input()
    print(count_edit_distance(first, second))

if __name__ == "__main__":
    main()

