#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == '__main__':
    s = str(input("Введите предложение: "))
    keycount = 0
    end = 0

    for n, e in enumerate(s):
        if e == "," and end == 0:
            comma1 = n
            end += 1
            continue
        if e == ",":
            comma2 = n

    if "comma1" in locals():
        if "comma2" in locals():
            print(s[comma1+1:comma2])
        else:
            print(s[comma1+1:])
