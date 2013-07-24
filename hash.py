#!/usr/bin/env python

import math
import sys

__USAGE__ = '''%s <file to hash>'''

def long_to_bytearray(l):
    return bytearray.fromhex(hex(l)[2:-1])

def SAMS_hash(data):
    bytes = bytearray(data)
    hashval = 0
    prime = (2 ** 32) - 5

    for i,b in enumerate(bytes):
        hashval ^= b
        if i % 8 == 0:
            hashval *= b
        if i % 6 == 0:
            hashval += prime

    hashval *= prime
    return hex(hashval & 0x0ffffffffffffffff)

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print __USAGE__ % sys.argv[0]
        exit(1)

    with open(sys.argv[1]) as f:
        data = f.read()
        print SAMS_hash(data)



















