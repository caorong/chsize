#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
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

# 常用词放上面
character_block = [eval(line.rstrip('\n')) for line in open(os.path.dirname(
                   os.path.realpath(__file__)) + '/character.py')]


DEFAUTL_SIZE = 1

def _check_size(char):
    char = u(char)
    if char < character_block[0][0] or \
            char > character_block[len(character_block) - 1][1]:
        return DEFAUTL_SIZE
    for i in character_block:
        if char < i[0]:
            continue
        if char <= i[1]:
            return i[2]
    return DEFAUTL_SIZE


def chlen(word):
    try:
        word = u(str(word))
    except:
        pass
    if isinstance(word, text_type):
        count = 0
        for char in word:
            size = _check_size(char)
            #  print(char, size)
            count += size
        return count
    else:
        return len(word)
