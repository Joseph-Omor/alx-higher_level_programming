#!/usr/bin/python3
"""
A program that prints numbers from 0 t0 98 in ascending order
"""
print(", ".join("{0:0>2}".format(numb) for numb in range(100)))
