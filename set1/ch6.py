"""
Break repeating-key XOR

It is officially on, now.
This challenge isn't conceptually hard, but it involves actual error-prone coding. The
other challenges in this set are there to bring you up to speed. This one is there to
qualify you. If you can do this one, you're probably just fine up to Set 6.

There's a file here. It's been base64'd after being encrypted with repeating-key XOR.

Decrypt it.

Here's how:

1. Let KEYSIZE be the guessed length of the key; try values from 2 to (say) 40.

2. Write a function to compute the edit distance/Hamming distance between two strings.
The Hamming distance is just the number of differing bits. The distance between:
    this is a test
and
    wokka wokka!!!
is 37. Make sure your code agrees before you proceed.

3. For each KEYSIZE, take the first KEYSIZE worth of bytes, and the second KEYSIZE
worth of bytes, and find the edit distance between them. Normalize this result by
dividing by KEYSIZE.

4. The KEYSIZE with the smallest normalized edit distance is probably the key. You
could proceed perhaps with the smallest 2-3 KEYSIZE values. Or take 4 KEYSIZE blocks
instead of 2 and average the distances.

5. Now that you probably know the KEYSIZE: break the ciphertext into blocks of KEYSIZE
length.

6. Now transpose the blocks: make a block that is the first byte of every block, and a
block that is the second byte of every block, and so on.

7. Solve each block as if it was single-character XOR. You already have code to do
this.

8. For each block, the single-byte XOR key that produces the best looking histogram is
the repeating-key XOR key byte for that block. Put them together and you have the key.

This code is going to turn out to be surprisingly useful later on. Breaking
repeating-key XOR ("Vigenere") statistically is obviously an academic exercise, a
"Crypto 101" thing. But more people "know how" to break it than can actually break it,
and a similar technique breaks something much more important.
"""

import math
import sys


def get_bits(a_str):
    """Represent each letter as 8 bits, 0-padded from left"""
    return "".join("{:0>8b}".format(ord(c)) for c in a_str)


def hamming_distance(str1, str2):
    """Get # of different bits between two equal-length strings"""
    b1 = get_bits(str1)
    b2 = get_bits(str2)

    diff_count = 0
    for i in range(len(b1)):
        if b1[i] != b2[i]:
            diff_count += 1

    return diff_count


def nCk(n, k):
    """How many combinations of n items exist when choosing k?"""
    f = math.factorial
    return f(n) // (f(k) * f(n - k))


def multi_hamming(*args):
    """Compute HD combinations for each pair of args, then average them"""
    if len(args) <= 1:
        raise "I only see {len(args)} argument(s). Need more!"

    else:
        total_dist = 0
        for i in range(0, len(args) - 1):
            for j in range(i + 1, len(args)):
                total_dist += hamming_distance(args[i], args[j])
        average = total_dist / nCk(len(args), 2)
        return average


def get_chunk(ct, keysize, window):
    """Get a chunk (window #) of a ciphertext"""
    return ct[window * keysize : (window + 1) * keysize]


def determine_keysize(ct):
    """Determine the keysize to which has the smallest avg hamming distance"""
    normalized_dists = {}
    for k in range(2, 41):
        chunk0 = get_chunk(ct, k, 0)
        chunk1 = get_chunk(ct, k, 1)
        chunk2 = get_chunk(ct, k, 2)
        chunk3 = get_chunk(ct, k, 3)
        dist = multi_hamming(chunk0, chunk1, chunk2, chunk3) / k
        normalized_dists[k] = dist
    sorted_dists = sorted(normalized_dists.items(), key=lambda x: x[1])
    for key, val in sorted_dists:
        print(key, val)

    # keysize is the first element of the first tuple
    return sorted_dists[0][0]


def break_ciphertext_into_blocks(ct, keysize):
    """Break up the ciphertext into blocks of size keysize"""
    ct_blocks = []
    num_blocks = len(ct) // keysize  # divide ct up into chunks of size keysize...
    for b in range(num_blocks):
        ct_blocks.append(get_chunk(ct, keysize, b))
    return ct_blocks


def break_repeating_xor(ct_file):
    with open(ct_file, "r") as f:
        ct = f.read()
    keysize = determine_keysize(ct)
    ct_blocks = break_ciphertext_into_blocks(ct, keysize)


if __name__ == "__main__":
    break_repeating_xor(sys.argv[1])
