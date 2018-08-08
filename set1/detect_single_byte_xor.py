"""
Detect single-character XOR

One of the 60-character strings in this file has been encrypted by single-character XOR.

Find it.

(Your code from #3 should help.)
"""
import sys

from single_byte_xor_cypher import decrypt_single_byte


def decrypt_strings_in_file(user_file):
    with open(user_file, "r") as f:
        for line in f:
            decrypt_single_byte(line)


if __name__ == "__main__":
    decrypt_strings_in_file(sys.argv[1])
