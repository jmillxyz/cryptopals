"""
Single-byte XOR cipher

The hex encoded string:
1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736

... has been XOR'd against a single character. Find the key, decrypt the
message.

You can do this by hand. But don't: write code to do it for you.

How? Devise some method for "scoring" a piece of English plaintext. Character
frequency is a good metric. Evaluate each output and choose the one with the
best score.

Achievement Unlocked
You now have our permission to make "ETAOIN SHRDLU" jokes on Twitter.
"""
import sys

# create scoring dict ranked by frequency, based on wikipedia
scoring = {
    " ": 1.650,
    "e": 1.270,
    "t": .906,
    "a": .817,
    "o": .751,
    "i": .697,
    "n": .675,
    "s": .633,
    "h": .609,
    "r": .599,
    "d": .425,
    "l": .403,
    "c": .278,
    "u": .276,
    "m": .241,
    "w": .236,
    "f": .223,
    "g": .202,
    "y": .197,
    "p": .193,
    "b": .149,
    "v": .98,
    "k": .77,
    "j": .15,
    "x": .15,
    "q": .10,
    "z": .7,
}


def decrypt_single_byte(hex_str):
    byte_str = bytes.fromhex(hex_str)

    max_score = 0.0
    key = ""
    phrase = ""
    for c in range(256):
        decoded_phrase = bytes([b ^ c for b in byte_str])
        score = sum([scoring.get(chr(d), 0) for d in decoded_phrase.lower()])
        if score > max_score:
            max_score = score
            phrase = decoded_phrase
            key = chr(c)
    try:
        return phrase.decode("utf-8")
    except UnicodeDecodeError:
        pass


if __name__ == "__main__":
    print(decrypt_single_byte(sys.argv[1]))
