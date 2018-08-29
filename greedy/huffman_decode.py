#!/usr/bin/python3
from huffman import Huffman

def read_decode_table():
    table = {}
    n, _ = map(int, input().split())

    for _ in range(n):
        char, code = input().split(": ")
        table[char] = code
    return table

def main():
    decode_table = read_decode_table()
    encoded_string = input()

    print(Huffman().set_decode_table(decode_table).decode(encoded_string))

if __name__ == "__main__":
    main()
