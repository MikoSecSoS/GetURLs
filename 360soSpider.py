#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import re
import sys
import time

import requests

from multiprocessing import Pool

"""
<div class="r"><a href="http://dq.tieba.com/p/4453884766" ping="/url?sa=t&amp;source=web&amp;rct=j&amp;url=http://dq.tieba.com/p/4453884766&amp;ved=2ahUKEwjo3KuK-O3iAhUKxLwKHVfEAgU4ChAWMAR6BAgDEAE"><h3 class="LC20lb">【图lou】qwqwqwqwqwqwqwq_蒂蓝墨吧_百度贴吧</h3><br><div class="TbwUpd"><cite class="iUh30">dq.tieba.com/p/4453884766</cite></div></a></div><div class="s"><div><span class="st"><span class="f">2016年4月3日 - </span>【图lou】<em>qwqwqwqwqwqwqwq</em>_蒂蓝墨吧_百度贴吧 ... 【图lou】<wbr><em>qwqwqwqwqwqwqwq</em>. 只看楼主收藏回复. 冥雅之舞 &middot; 吧主. 9. 该楼层疑似违规已被系统&nbsp;...</span></div></div></div></div><!--n--></div><span id="fld"></span><div class="g"><!--m--><div data-hveid="CAQQAA" data-ved="2ahUKEwjo3KuK-O3iAhUKxLwKHVfEAgU4ChAVKAAwBXoECAQQAA"><div class="rc"><div class="r"><a href="https://steamid.uk/group/10720663" ping="/url?sa=t&amp;source=web&amp;rct=j&amp;url=https://steamid.uk/group/10720663&amp;ved=2ahUKEwjo3KuK-O3iAhUKxLwKHVfEAgU4ChAWMAV6BAgEEAE"><h3 class="LC20lb">SteamID » Group &gt; qwqwqwqwqwqwqwq &gt; D.F.A.K</h3><br><div class="TbwUpd"><cite class="iUh30">https://steamid.uk/group/10720663</cite></div></a><span><div class="action-menu ab_ctl"><a class="GHDvEf ab_button" href="#" id="am-b15" aria-label="结果选项" aria-expanded="false" aria-haspopup="true" role="button" jsaction="m.tdd;keydown:m.hbke;keypress:m.mskpe" data-ved="2ahUKEwjo3KuK-O3iAhUKxLwKHVfEAgU4ChDsHTAFegQIBBAC"><span class="mn-dwn-arw"></span></a><div class="action-menu-panel ab_dropdown" role="menu" tabindex="-1" jsaction="keydown:m.hdke;mouseover:m.hdhne;mouseout:m.hdhue" data-ved="2ahUKEwjo3KuK-O3iAhUKxLwKHVfEAgU4ChCpHzAFegQIBBAD"><ol><li class="action-menu-item ab_dropdownitem" role="menuitem"><a class="fl" href="https://webcache.googleusercontent.com/search?q=cache:g83zmSxa5AMJ:https://steamid.uk/group/10720663+&amp;cd=16&amp;hl=zh-CN&amp;ct=clnk&amp;gl=us" ping="/url?sa=t&amp;source=web&amp;rct=j&amp;url=https://webcache.googleusercontent.com/search%3Fq%3Dcache:g83zmSxa5AMJ:https://steamid.uk/group/10720663%2B%26cd%3D16%26hl%3Dzh-CN%26ct%3Dclnk%26gl%3Dus&amp;ved=2ahUKEwjo3KuK-O3iAhUKxLwKHVfEAgU4ChAgMAV6BAgEEAQ">网页快照</a></li></ol></div></div></span><a class="fl" href="https://translate.google.com/translate?hl=zh-CN&amp;sl=en&amp;u=https://steamid.uk/group/10720663&amp;prev=search" ping="/url?sa=t&amp;source=web&amp;rct=j&amp;url=https://translate.google.com/translate%3Fhl%3Dzh-CN%26sl%3Den%26u%3Dhttps://steamid.uk/group/10720663%26prev%3Dsearch&amp;ved=2ahUKEwjo3KuK-O3iAhUKxLwKHVfEAgU4ChDuATAFegQIBBAG">翻译此页</a></div>
"""

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
            "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36"
        }
        filename = word + " " + now_time + ".txt"
        url = "https://www.so.com/s?q={}&pn={}".format(word, page)
        req = requests.get(url, headers=hd)
        if page != 1:
        	now_page = re.findall("<strong>(.*?)</strong>", req.text)[0]
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
    bingSpider = BingSpider()
    bingSpider.word = word
    bingSpider.main()
