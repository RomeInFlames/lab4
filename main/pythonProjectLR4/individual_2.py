#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == '__main__':
    s = str(input("Введите предложение: "))
    keycount = 0
    end = 0
    n = 0

    while n < len(s):
        if s[n] == "," and end == 0:
            comma1 = n
            end += 1
            continue
        if s[n] == ",":
            comma2 = n
        n += 1

    if "comma1" in locals():
        if "comma2" not in locals():
            print(s[comma1+1:comma2])
        else:
            print(s[comma1+1:])