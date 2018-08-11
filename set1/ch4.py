"""
Detect single-character XOR

One of the 60-character strings in this file has been encrypted by single-character XOR.

Find it.

(Your code from #3 should help.)
"""
import sys

from set1.ch3 import decrypt_single_byte, scoring


def decrypt_strings_in_file(user_file):
    with open(user_file, "r") as f:
        # add most-promising line combo to the list if we can decode it to utf-8
        decrypted = [
            decrypt_single_byte(line) for line in f if decrypt_single_byte(line)
        ]

    max_score = 0
    phrase = ""
    for pt in decrypted:
        score = sum(scoring.get(p, 0) for p in pt.lower())
        if score > max_score:
            max_score = score
            phrase = pt
    return phrase


if __name__ == "__main__":
    print(decrypt_strings_in_file(sys.argv[1]))
