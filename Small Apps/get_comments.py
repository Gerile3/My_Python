#!/usr/bin/env python3
from os import path
from shutil import copy


def main():
    """Prints out comments in a file"""
    my_comments = []
    if path.exists("file.py"):
        src = path.realpath("file.py")
    copy(src, "path\\to\\file")
    with open("deneme.txt") as infile:
        for line in infile:
            if line.startswith("#"):
                my_comments.append(line.strip('\n'))
    print("\n".join(my_comments))


if __name__ == "__main__":
    main()
