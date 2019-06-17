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

class So:

    @staticmethod
    def getUrls(page):
        now_time = time.strftime('%Y-%m-%d', time.localtime(time.time()))
        hd = {
            "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3",
            "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36"
        }
        filename = word + " " + now_time + ".txt"
        url = "https://www.so.com/s?q={}&pn={}".format(word, page)
        req = requests.get(url, headers=hd)
        if page != 1:
        	now_page = re.findall("</a><strong>(.*?)</strong>", req.text)[0]
	        if int(now_page) != page:
	        	return
        urls_titles = re.findall("<h3  class=\"res-title\"><a href=\"(.*?)\".*?>(.*?)</a></h3>", req.text)
        data = []
        for url, title in urls_titles:
            title = title.replace("<em>", "").replace("</em>", "")
            data.append({
                "title": title,
                "url": url
            })
            print(title, url)
        download(filename, data)

    def main(self):
        pool = Pool()
        pool.map(self.getUrls, [i for i in range(1, 65)])


if __name__ == "__main__":
    if len(sys.argv) == 2:
        word = sys.argv[1]
    else:
        word = input("Please input search content: ")
    so = So()
    so.word = word
    so.main()
