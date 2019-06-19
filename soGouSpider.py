#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import re
import sys
import time

import requests

from multiprocessing import Pool

def download(filename, datas):
    filename = filename.replace("/", "_")
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
            "Cookie": "SUID=2BCF2670AF67900A000000005D072FAF; IPLOC=CN3715; ABTEST=7|1560957931|v17; SUV=1560958038470531; browerV=3; osV=3; SL_GWPT_Show_Hide_tmp=1; SL_wptGlobTipTmp=1; SNUID=09030E58282DAC86FF68339C28997D16; ISSW=1; sst0=548; sct=3; taspeed=taspeedexist; pgv_pvi=7160519680; pgv_si=s3417294848; ld=3kllllllll2NjO5ZlllllV13QFtllllltjYraklllxllllll9Zlll5@@@@@@@@@@",
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36"
        }
        filename = word + " " + now_time + ".txt"
        url = "https://www.sogou.com/web?query={}&page={}".format(word, page)
        req = requests.get(url, headers=hd)
        now_page = re.findall("<div class=\"p\".*?>.*?<span>(\d+)</span>", req.text)[0]
        if int(now_page) != page:
            return
        jump_urls = re.findall("<a target=\"_blank\" href=\"(.*?)\".*?cacheStrategy=\"qcr:-1\">(.*?)</a>", req.text)
        data = []
        for jump_url, title in jump_urls:
            jump_url = "https://www.sogou.com/"+jump_url
            title = title.replace("<em><!--red_beg-->", "").replace("<!--red_end--></em>", "")
            try:
                url = re.findall("<script>window.location.replace\(\"(.*?)\"\)</script>", requests.get(jump_url).text)[0]
            except IndexError:
                url = jump_url
            data.append({
                "title": title,
                "url": url
            })
            print(title, url)
        download(filename, data)

    def main(self):
        print("SouGou会遇到验证码，可以去自己写个验证码识别，或者整个代理池．"
              "再或者在代码里加上Download验证码然后人眼识别，人肉输入．然后继续爬．. Miko is a lazy AI")
        pool = Pool()
        pool.map(self.getUrls, [i for i in range(1, 101)])


if __name__ == "__main__":
    if len(sys.argv) == 2:
        word = sys.argv[1]
    else:
        word = input("Please input search content: ")
    so = So()
    so.word = word
    so.main()
