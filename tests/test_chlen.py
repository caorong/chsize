#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import os
sys.path.insert(0, os.path.abspath(__file__+"/../.."))

from chsize import chlen

PY3 = sys.version_info[0] == 3
if PY3:
    text_type = str
    string_types = (str,)

    def u(s):
        return s
else:
    text_type = unicode  # noqa
    string_types = (str, unicode)  # noqa

    def u(s):
        if not isinstance(s, text_type):
            s = s.decode("utf-8")
        return s


def test_num():
    assert 5 == chlen(12345)


def test_chinese():
    assert 10 == chlen("阿斯顿发过")


def test_english():
    assert 5 == chlen("asdfg")


def test_half_english_symbol():
    assert 6 == chlen("!#$%^&")


def test_full_chinese_symbol1():
    assert 20 == chlen("！＃¥％……&＊（）——＋")


def test_full_chinese_symbol2():
    check_everyword("《》？：“”｛｝｜")
    assert 16 == chlen("《》？：“”｛｝｜")


def test_full_chinese_symbol2_test():
    #  check_everyword("《")
    assert 2 == chlen("《")


def check_everyword(word):
    for i in u(word):
        print(i, chlen(i))


if __name__ == "__main__":
    test_full_chinese_symbol2()
