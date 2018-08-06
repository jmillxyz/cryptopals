"""
Fixed XOR

Write a function that takes two equal-length buffers and produces
their XOR combination.

If your function works properly, then when you feed it the string:
1c0111001f010100061a024b53535009181c

after hex decoding, and when XOR'd against:
686974207468652062756c6c277320657965

should produce:
746865206b696420646f6e277420706c6179
"""

import base64
import sys

from hex_to_base64 import hex_to_b64


def xor_buffers(buf1, buf2):
    b64_buf1 = hex_to_b64(buf1)
    b64_buf2 = hex_to_b64(buf2)

    b64_list1 = [c for c in b64_buf1]
    b64_list2 = [c for c in b64_buf2]

    b64_xor_list = [a ^ b for a, b in zip(b64_list1, b64_list2)]

    hex_xor = "".join(b64_xor_list)
    print(hex_xor)


if __name__ == "__main__":
    print(xor_buffers(sys.argv[1], sys.argv[2]))
