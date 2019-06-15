#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import sys
import glob
import time

def main(number):
    newtext = []
    args = [*sys.argv,][1:]

    if number == '1':
        new_file_name = input("[+] Please new file name: ")
    start = time.time()
    if len(args) == 0:
        file_names = glob.glob(input('[+] Please input path：'))
        for file_name in file_names:
            with open(file_name,'r') as text:
                [newtext.append(i) for i in text.readlines() if i not in newtext]
                if "new_file_name" in dir(): file_name = new_file_name
        with open(file_name, 'w') as f:
            f.write(''.join(newtext))
    else:
        file_names = []
        [file_names.extend(glob.glob(arg)) for arg in args]
        for file_name in file_names:
            with open(file_name, 'r') as text:
                if "new_file_name" in dir():
                    file_name = new_file_name
                    with open(file_name, 'a+') as ntext:
                        [newtext.append(i) for i in ntext.readlines() if i not in newtext]
                [newtext.append(i) for i in text.readlines() if i not in newtext]
            with open(file_name, 'w') as f:
                if newtext != []:
                    f.write(''.join(newtext))
                else:
                    print("Not Repeat.")
    return time.time() - start

if __name__ == '__main__':
    number = input("1.去重后保存到新文件\n2.去重后保存到原文件\n[*] Please choose number: ")
    if number == '1' or number == '2':
        print("[*] Time consuming: {:.2f}s".format(main(number)))
    else:
        print("[!] Please input 1 or 2")