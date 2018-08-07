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


def decrypt_single_byte(hex_str):
    byte_str = bytes.fromhex(hex_str)

    # create scoring dict ranked by frequency
    scoring = dict(zip(b"etaoinshrdlcumwfgypbvkjxqz",list(range(26,0,-1))))

    max_score = 0
    key = ""
    phrase = b""
    for c in range(ord("A"), ord("Z")):
        decoded_phrase = bytes([b ^ c for b in byte_str])
        score = sum([scoring.get(d, 0) for d in decoded_phrase.lower()])
        if score > max_score:
            max_score = score
            phrase = decoded_phrase
            key = chr(c)
    print(f"decryption key: {key}")
    print("phrase: ", end="")
    print(phrase)


if __name__ == "__main__":
    decrypt_single_byte(sys.argv[1])
