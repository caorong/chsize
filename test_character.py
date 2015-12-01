#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import os
import subprocess
from fabric.api import local

import logging
#  from sets import Set

#  http://stackoverflow.com/questions/10959227/how-to-distinguish-whether-a-word-is-half-width-or-full-width/10959274
#  \u00F01-\uFF60 and \uFFE0-\uFFE6 are fullwidth, while \uFF61-\uFFDC and
# \uFFE8-\uFFEE are halfwidth.

# http://unicode-table.com/cn/blocks/cjk-unified-ideographs/
# 4E00—9FFF

# will cause error


def main2():
    for i in range(int("4E00", 16), int('9FFF', 16) + 1):
        p = subprocess.Popen(['/bin/bash', 'test.sh', unichr(i)],
                             stdout=subprocess.PIPE,
                             stderr=subprocess.PIPE)
        out, err = p.communicate()
        size = int(out.split(':')[2])
        if size is not 2:
            print(out, unichr(i), i)


def test_range(start, end):
    for i in range(int(start, 16), int(end, 16) + 1):
        out = local(u'/bin/bash test.sh {}'.format(unichr(i)), capture=True)
        size = int(out.split(':')[2])
        if size is not 2:
            logging.info("{}".format((out, unichr(i), i)))


def _hex(c):
    #  print('\u' + hex(c)[2:])
    return '\u{0}'.format(hex(c)[2:])


def iter_range_withoutput(start, end):
    logging.basicConfig(filename='{}-{}.log'.format(start, end),
                        level=logging.INFO)
    result = []
    last = None
    for i in range(int(start, 16), int(end, 16) + 1):
        out = local(u'/bin/bash test.sh {}'.format(unichr(i)), capture=True)
        size = int(out.split(':')[2])
        if not last:
            last = (i, size)
            pass
        elif last[1] != size:
            print("{} -> {} = {}".format(_hex(last[0]), _hex(i - 1), last[1]))
            logging.info("{} -> {} = {}".format(_hex(last[0]), _hex(i - 1),
                         last[1]))
            result.append((last[0], i - 1, last[1]))
            last = (i, size)
    for i in result:
        #  (u'\uFFE0', u'\uFFE6', 2),
        print("(u'{}', u'{}', {}),".format(_hex(i[0]), _hex(i[1]), i[2]))
        print("('{}', '{}', {}),".format(i[0], i[1], i[2]))
        logging.info("(u'{}', u'{}', {}),".format(_hex(i[0]), _hex(i[1]),
                     i[2]))
    generate_character_block_file(result)


def generate_character_block_file(result):
    characterFile = os.path.dirname(os.path.realpath(__file__)) +\
        '/chsize/character.py'

    # read original file
    orig_characters = [eval(line.rstrip('\n')) for line in open(characterFile)]

    total_characters = set(orig_characters)

    for i in result:
        total_characters.add((unichr(i[0]), unichr(i[1]), i[2]))

    # write to file
    with open(characterFile, 'w') as f:
        for i in sorted(total_characters, key=lambda x: x[0]):
            f.write(str(i) + '\n')


def main():
    #  http://unicode-table.com/cn/blocks/halfwidth-and-fullwidth-forms/
    #  test_range('FF00', 'FFEF')
    #  test_range('4E00', '9FFF')

    #  http://unicode-table.com/cn/blocks/cjk-symbols-and-punctuation/
    iter_range_withoutput('3000', '303F')

if __name__ == "__main__":
    #  generate_character_block_file([(12288, 12329, 2), (12330, 12335, 3)])
    #  _hex(12329)
    main()
