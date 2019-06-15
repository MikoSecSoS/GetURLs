#!/usr/bin/env python
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

class BaiduSpider:

    @staticmethod
    def getUrls(page):
        now_time = time.strftime('%Y-%m-%d', time.localtime(time.time()))
        filename = word + " " + now_time + ".txt"
        url = "https://www.baidu.com/s?wd={}&pn={}".format(word, page)
        req = requests.get(url, headers={"user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36"})
        now_page = re.findall("<strong>.*?<span class=\"pc\">(.*?)</span></strong>", req.text)[0]
        if now_page == 1 and page != 0:
            return
        jump_urls = re.findall("<div.*?><h3.*?><a[\s\S]*?href.*?\"(.*?)\"[\s\S]*?>(.*?)</a></h3><div", req.text)
        data = []
        for jump_url, title in jump_urls:
            if jump_url[:4] != "http":
                continue
            title = title.replace("<em>", "").replace("</em>", "")
            url = requests.get(jump_url, allow_redirects=False).headers["Location"]
            data.append({
                "title": title,
                "url": url
            })
            print(title, url)
        download(filename, data)
        return data

    def main(self):
        pool = Pool()
        pool.map(self.getUrls, [i*10 for i in range(100)])

if __name__ == "__main__":
    if len(sys.argv) == 2:
        word = sys.argv[1]
    else:
        word = input("Please input search content: ")
    baiduSpider = BaiduSpider()
    baiduSpider.word = word
    baiduSpider.main()