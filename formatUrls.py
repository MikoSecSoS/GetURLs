#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
import glob
import time

def formatUrls(path):
    if not os.path.exists("urls.txt"):
        file = open("urls.txt", "w")
        file.close()
    if os.path.exists(path):
        file = open(path, "r")
        with open("urls.txt", "a") as f:
            for line in file.readlines():
                url = line[line.index("'url': '")+8:-3]
                print(url)
                f.write(url+"\n")


if __name__ == "__main__":
    paths = [*sys.argv,][1:]
    if not paths:
        paths = [input('[+] Please input path：')]
    for path in paths:
        path = glob.glob(path)
        for p in path:
            formatUrls(p)