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

class BingSpider:

    @staticmethod
    def getUrls(page):
        now_time = time.strftime('%Y-%m-%d', time.localtime(time.time()))
        hd = {
            "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3",
            "accept-language": "zh-CN,zh;q=0.9",
            "alexatoolbar-alx_ns_ph": "AlexaToolbar/alx-4.0.3",
            "cache-control": "max-age=0",
            "upgrade-insecure-requests": "1",
            "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36"
        }
        filename = word + " " + now_time + ".txt"
        url = "https://cn.bing.com/search?q={}&ensearch=1&first={}".format(word, page)
        req = requests.get(url, headers=hd)
        if "There are no results for" in req.text:
            return
        urls_titles = re.findall("<h2><a.*?href=\"(.*?)\".*?>(.*?)</a></h2>", req.text)
        data = []
        for url, title in urls_titles:
            title = title.replace("<strong>", "").replace("</strong>", "")
            data.append({
                "title": title,
                "url": url
            })
            print(title, url)
        download(filename, data)

    def main(self):
        pool = Pool()
        pool.map(self.getUrls, [0] + [8+i*10 for i in range(100)])


if __name__ == "__main__":
    if len(sys.argv) == 2:
        word = sys.argv[1]
    else:
        word = input("Please input search content: ")
    bingSpider = BingSpider()
    bingSpider.word = word
    bingSpider.main()
