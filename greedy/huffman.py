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

        def xstr(s):
            return '' if s is None else str(s)

        def __init__(self, data):
            self.data = data
            self.left = None
            self.right = None
           
        def __lt__(self, other):
            return self.xstr(self.data) < self.xstr(other.data)

        def __repr__(self):
            return self.data

    def __init__(self, string=None):
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
     
    def build_encode_tree(self, queue):
        for _ in range(queue.qsize() - 1):
            lp, lnode  = queue.get()
            rp, rnode  = queue.get()
           
            queue.put((lp + rp, self.Node.build_parent(None, lnode, rnode)))

        _, self.tree = queue.get()
        return self
 
    def add_char_to_tree(self, char, code):
        self.tree = current_node = self.tree
        for c in code:
            if c == '0':
                if not current_node.left:
                    current_node.left = self.Node(None)
                current_node = current_node.left 
            elif c == '1':
                if not current_node.right:
                    current_node.right = self.Node(None)
                current_node = current_node.right

        current_node.data = char

    def build_decode_tree(self):
        self.tree = self.Node(None)

        for pair in self.table.items():
            self.add_char_to_tree(*pair)
        return self 

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

            self.build_encode_tree(queue)
            self.build_table(self.tree)
        elif len(freq) == 1:
            self.table[self.string[0]] = '1'

        return self
    
    def decode(self, encoded_string):
        decoded_string = [] 
        current_node = self.tree

        for c in encoded_string:
            if c == '0':
                current_node = current_node.left
            elif c == '1':
                current_node = current_node.right

            if current_node.data is not None:
                decoded_string.append(current_node.data)
                current_node = self.tree

        return ''.join(decoded_string)


    def set_decode_table(self, table):
        self.table = table
        self.build_decode_tree()
        return self

    def encode_table(self):
        return self.table

    def encoded_string(self):
        return ''.join([self.table[c] for c in self.string])


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
