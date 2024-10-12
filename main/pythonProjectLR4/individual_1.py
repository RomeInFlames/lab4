#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == '__main__':
    s = str(input("Введите предложение: "))
    keycount = 0
    n = 0

    while n < len(s):
        if s[n] == "н":
            if s[n+1] == "н":
                keycount += 1
                n += 1
        n += 1

    if keycount == 0:
        exit(1)

    s = keycount * "нн, "
    s = s[:len(s)-2] + ""

    print(f"{s}")