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
import binascii
import sys


def xor_buffers(buf1, buf2):
    byte_buf1 = bytes.fromhex(buf1)
    byte_buf2 = bytes.fromhex(buf2)

    byte_list1 = [c for c in byte_buf1]
    byte_list2 = [c for c in byte_buf2]

    xord_bytes = bytes([a ^ b for a, b in zip(byte_list1, byte_list2)])

    return binascii.hexlify(xord_bytes).decode("utf-8")


if __name__ == "__main__":
    print(xor_buffers(sys.argv[1], sys.argv[2]))
