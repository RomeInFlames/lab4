#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == '__main__':
    word_1 = "прроцесор"
    word_2 = "теекстовыйфайл"
    word_3 = "програма и аллгоритм"
    word_4 = "процесор и паммять"

    word_1 = word_1[:1] + word_1[2:6] + "c" + word_1[6:]
    word_2 = word_2[:1] + word_2[2:10] + " " + word_2[10:]
    word_3 = word_3[:7] + "м" + word_3[7:12] + word_3[13:]
    word_4 = word_4[:6] + "c" + word_4[6:14] + word_4[15:]

    print(f"{word_1}\n{word_2}\n{word_3}\n{word_4}")