#!/usr/bin/env python3
"""
Replace each plaintext letter with a different one fixed number of places
up or down the alphabet
e.g: "Hello my friend" > "ifmmp!nz!gsjfoe"
"""


def cipher(text, shift=1):
    result = ""
    for i, j in enumerate(text):
        result += chr(ord(j) + (shift + (i + 1)))
    return result


def decipher(text, shift=1):
    result = ""
    for i, j in enumerate(text):
        result += chr(ord(j) - (shift + (i + 1)))
    return result


if __name__ == "__main__":
    text = input("Enter message to cipher: ")
    shift = input("Enter Initial shift number (default=1): ")
    if shift:
        result = cipher(text, int(shift))
        original = decipher(result, int(shift))
    else:
        result = cipher(text)
        original = decipher(result)
    print("Ciphered message:", result)
    print("Original message:", original)

    # Todo:
    # Add division of message support for different carriers
