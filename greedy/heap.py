#!/usr/bin/python3
class PriorityQueue:

    def __init__(self, queue=[]):
        self.queue = []
        for el in queue:
            self.insert(el)

    def insert(self, el):
        self.queue.append(el)
        self.sift_up()
        return self

    def extract_max(self):
        self.swap(0, len(self.queue) - 1)
        res = self.queue.pop()
        self.sift_down()
        return res

    def swap(self, n, m):
        self.queue[n], self.queue[m] = self.queue[m], self.queue[n]

    def sift_up(self):
        current = len(self.queue) - 1

        while current != 0:
            parent = current // 2 - (current + 1) % 2
            if self.queue[current] > self.queue[parent]:
                self.swap(current, parent)
                current = parent
            else:
                break

    def get_max_child(self, left, right):
        if self.queue[left] > self.queue[right]:
            res = left, self.queue[left]
        else:
            res = right, self.queue[right]
        return res

    def sift_down(self):
        current = 0
        size = len(self.queue)

        import pdb; pdb.set_trace()
        while True:
            left, right = current * 2 + 1, current * 2 + 2

            if right < size:
                index, value = self.get_max_child(left, right)
            elif left < size:
                index, value = left, self.queue[left]
            else:
                break

            if self.queue[current] > value:
                break
            self.swap(current, index)
            current = index

def main():
    n = int(input())
    q = PriorityQueue()
    cache = []

    for _ in range(n):
        command = input().split(' ')
        if command[0] == "Insert":
            q.insert(int(command[1]))
        elif command[0] == "ExtractMax":
            cache.append(q.extract_max())

    print('\n'.join(str(el) for el in cache))


if __name__ == "__main__":
    main()
