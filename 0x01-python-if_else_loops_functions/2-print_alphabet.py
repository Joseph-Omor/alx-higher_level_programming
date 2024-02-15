#!/usr/bin/python3
"""
This code prints the ASCII alphabet in lowercase
not followed by a new line.
"""
for char in range(ord('a'), ord('z') + 1):
    print(chr(char), end="")
