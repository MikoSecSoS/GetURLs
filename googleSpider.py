#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import re
import sys
import time

import requests

from multiprocessing import Pool

def download(filename, datas):
    if not os.path.exists(filename):
        f = open(filename, "w")
        f.close()
    with open(filename, "a") as f:
        for data in datas:
            f.write(str(data) + "\n")

class GoogleSpider:

    @staticmethod
    def getUrls(page):
        now_time = time.strftime('%Y-%m-%d', time.localtime(time.time()))
        filename = word + " " + now_time + ".txt"
        url = "https://www.google.com/search?q={}&start={}".format(word, page)
        req = requests.get(url, headers={"user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36"})
        if "找不到和您查询的" in req.text:
            return
        urls_titles = re.findall("<div class=\"r\"><a href=\"(.*?)\".*?><h3.*?>(.*?)</h3>", req.text)
        data = []
        for url, title in urls_titles:
            data.append({
                "title": title,
                "url": url
            })
            print(title, url)
        download(filename, data)

    def main(self):
        [self.getUrls(i*10) for i in range(100)]


if __name__ == "__main__":
    if len(sys.argv) == 2:
        word = sys.argv[1]
    else:
        word = input("Please input search content: ")
    googleSpider = GoogleSpider()
    googleSpider.word = word
    googleSpider.main()
