import pytest

from set1 import ch1, ch2, ch3, ch4, ch5, ch6


def test_ch1():
    hex_str = (
        "49276d206b696c6c696e6720796f757220627261696e206c"
        "696b65206120706f69736f6e6f7573206d757368726f6f6d"
    )
    base_64_str = "SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t"

    assert ch1.hex_to_b64(hex_str) == base_64_str


def test_ch2():
    hex1 = "1c0111001f010100061a024b53535009181c"
    hex2 = "686974207468652062756c6c277320657965"
    expected = "746865206b696420646f6e277420706c6179"

    assert ch2.xor_buffers(hex1, hex2) == expected


def test_ch3():
    hex_str = "1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736"
    plaintext = "Cooking MC's like a pound of bacon"

    assert ch3.decrypt_single_byte(hex_str) == plaintext


def test_ch4():
    plaintext = "Now that the party is jumping\n"

    assert ch4.decrypt_strings_in_file("set1/4.txt") == plaintext


def test_ch5():
    plaintext = (
        "Burning 'em, if you ain't quick and nimble\nI go crazy when I hear a cymbal"
    )
    expected = (
        "0b3637272a2b2e63622c2e69692a23693a2a3c6324202d623d63343c2a26226324272765272"
        "a282b2f20430a652e2c652a3124333a653e2b2027630c692b20283165286326302e27282f"
    )

    assert ch5.repeating_xor(plaintext) == expected


def test_ch6():
    str1 = "this is a test"
    str2 = "wokka wokka!!!"

    assert ch6.hamming_distance(str1, str2) == 37
