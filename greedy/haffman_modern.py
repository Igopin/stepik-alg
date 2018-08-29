#!/usr/bin/python3
from queue import PriorityQueue

class Huffman:
    class Node:

        @classmethod
        def build_parent(cls, data, left, right):
            node = cls(data)
            node.left = left
            node.right = right
            return node

        def __init__(self, data):
            self.data = data
            self.left = None
            self.right = None
           
        def __lt__(self, other):
            return self.data < other.data

        def __repr__(self):
            return self.data

    def __init__(self, string):
        self.string = string
        self.tree = None
        self.table = {}
        self.current_seq = []

    def get_frequency(self):
        freq = {}
        for c in self.string:
            if c in freq:
                freq[c] += 1
            else:
                freq[c] = 1
        return freq
     
    def build_tree(self, queue):
        for _ in range(queue.qsize() - 1):
            lp, lnode  = queue.get()
            rp, rnode  = queue.get()
           
            queue.put((lp + rp, self.Node.build_parent('', lnode, rnode)))

        _, self.tree = queue.get()

    def build_table(self,  node):
        if not node:
            self.current_seq.pop()
            return

        self.current_seq.append(0)
        self.build_table(node.left)
       
        if bool(node.data):
            self.table[node.data] = ''.join(str(e) for e in self.current_seq)
        
        self.current_seq.append(1)
        self.build_table(node.right) 
        
        if self.tree != node:
            self.current_seq.pop()
 

    def encode(self):
        freq = self.get_frequency()

        if len(freq) > 1:
            queue = PriorityQueue()

            for c, f in freq.items():
                queue.put((f, self.Node(c))) 

            self.build_tree(queue)
            self.build_table(self.tree)
        elif len(freq) == 1:
            self.table[self.string[0]] = '1'

        return self


    def encode_table(self):
        return self.table

    def encoded_string(self):
        return ''.join([self.table[c] for c in self.string])


def get_frequency(string):
    return freq


def main():
    string = input()

    h = Huffman(string).encode()
    t = h.encode_table()
    s = h.encoded_string()
    print("{} {}".format(len(t), len(s)))
    print('\n'.join(["{}: {}".format(key, value) for key, value in sorted(t.items())]))
    print(s)

if __name__ == "__main__":
    main()
