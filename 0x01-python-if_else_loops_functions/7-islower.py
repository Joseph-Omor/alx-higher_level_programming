#!/usr/bin/python3
""" A function that checks for lower character"""
def islower(c):
    if ord(c) > 96 and ord(c) < 123:
        return True
    return False
