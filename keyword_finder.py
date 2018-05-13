#! /Usr/bin/python
# Scott Little
# CPSC 3400
# 4/17/18
# Project 1

from __future__ import print_function
import sys
import re


def _main():
    # keyword file separates each keyword by a space #
    if (sys.argv is 1) and os.path.exists(sys.argv[1]):
        with open(sys.argv[1], "r") as keywords:
            for line in keywords:
                keyword_list = line.split()
    else:
        with open("keywords.txt", "r") as keywords:
            for line in keywords:
                keywords_list = line.split()

    titles_list = []
    found_list = []
    with open("titles.txt", "r") as titles:
        for line in titles:
            for keyword in keywords_list:
                for i in re.findall("(?<!\\w|\\d){0}[^a-rt-z\\d]".format(keyword),
                                    line, re.IGNORECASE):
                        found_list.append(keyword + ": " + line[:-1])

    found_list.sort()
    for element in found_list:
        print(element)

if __name__ == '__main__':
    _main()
