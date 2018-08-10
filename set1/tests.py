import pytest

import hex_to_base64
import fixed_xor
import single_byte_xor_cypher
import detect_single_byte_xor
import repeating_key_xor


def test_ch1():
    hex_str = (
        "49276d206b696c6c696e6720796f757220627261696e206c"
        "696b65206120706f69736f6e6f7573206d757368726f6f6d"
    )
    base_64_str = "SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t"

    assert hex_to_base64.hex_to_b64(hex_str) == base_64_str


def test_ch2():
    hex1 = "1c0111001f010100061a024b53535009181c"
    hex2 = "686974207468652062756c6c277320657965"
    expected = "746865206b696420646f6e277420706c6179"

    assert fixed_xor.xor_buffers(hex1, hex2) == expected


def test_ch3():
    hex_str = "1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736"
    plaintext = "Cooking MC's like a pound of bacon"

    assert single_byte_xor_cypher.decrypt_single_byte(hex_str) == plaintext


def test_ch4():
    plaintext = "Now that the part is jumping\n"

    assert detect_single_byte_xor.decrypt_strings_in_file("4.txt") == plaintext


def test_ch5():
    plaintext = (
        "Burning 'em, if you ain't quick and nimble\nI go crazy when I hear a cymbal"
    )
    expected = (
        "0b3637272a2b2e63622c2e69692a23693a2a3c6324202d623d63343c2a26226324272765272"
        "a282b2f20430a652e2c652a3124333a653e2b2027630c692b20283165286326302e27282f"
    )

    assert repeating_key_xor.repeating_xor(plaintext) == expected
