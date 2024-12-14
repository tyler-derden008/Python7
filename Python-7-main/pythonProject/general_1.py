#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == "__main__":
    a = set("aeiouyAEIOUY")
    count_1 = 0

    b = str(input())
    for b in a:
        if b in a:
            count_1 += 1

    print("Vowels :", count_1)
