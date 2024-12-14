#!/usr/bin/env python3
# -*- coding: utf-8 -*-


if __name__ == "__main__":
    A = {"apple", "banana", "cherry"}
B = {"banana", "kiwi", "orange"}
C = {"cherry", "fig", "grape"}
D = {"kiwi", "lemon", "melon"}

# Вычисляю X = (A ∩ C) ∪ B
X = (A.intersection(C)).union(B)
print("X =", X)

# Вычисляю дополнения
universal_set = A.union(B).union(C).union(D)

A_complement = universal_set - A
B_complement = universal_set - B

# Вычисляю Y = (A' ∩ B') / (C ∪ D)
Y = (A_complement.intersection(B_complement)).difference(C.union(D))
print("Y =", Y)
