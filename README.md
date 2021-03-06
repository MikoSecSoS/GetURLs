<h1 align="center">Welcome to GetURLs 👋</h1>
<p>
  <img src="https://img.shields.io/badge/version-0.1.1-blue.svg?cacheSeconds=2592000" />
  <a href="https://github.com/MikoSecSoS/readme-md-generator#readme">
    <img alt="Documentation" src="https://img.shields.io/badge/documentation-yes-brightgreen.svg" target="_blank" />
  </a>
  <a href="https://github.com/MikoSecSoS/readme-md-generator/graphs/commit-activity">
    <img alt="Maintenance" src="https://img.shields.io/badge/Maintained%3F-yes-green.svg" target="_blank" />
  </a>
  <a href="https://github.com/MikoSecSoS/readme-md-generator/blob/master/LICENSE">
    <img alt="License: MIT" src="https://img.shields.io/badge/License-MIT-yellow.svg" target="_blank" />
  </a>
</p>

> 提供搜索关键字,在各大搜索引擎进行搜索并采集搜索到的URL.

### 🏠 [Homepage](https://github.com/MikoSecSoS/GetURLs#readme)

## Prerequisites

- Python &gt;=3.0

## Install

```sh
git clone https://github.com/MikoSecSoS/GetURLs.git
cd GetURLs && pip3 install -r requirements.txt
```

## Files

**xxxSpider.py** -- 采集xxx搜索引擎的urls

- Use: python3 xxxSpider.py 关键字
- python3 baiduSpider.py Miko

**formatUrls.py** -- 取出xxxSpider.py爬取到的URL**#支持正则**

- Use: python3 formatUrls.py path
- python3 fotmatUrls.py *.txt

**removeRepeat.py** -- 文本去重

- Use: python3 removeRepeat.py path
- python3 removeRepeat.py *.txt

## Other

因为Miko是lazy的,所以还有很多搜索引擎的爬虫的没写(其实之前写了一些的,不过被万恶的手残rm掉了.

还有就是最近Code很忙,没时间陪Miko,导致Miko心情有些低落然后写出来的代码非常的ugly.

待Code有时间陪伴Miko时,Miko会对代码进行重构,把代码打扮的漂漂亮亮的.

另外如果你使用的Windows系统可能会出现一些玄学异常，请自行修改代码．

如果您是Linux玩家可以正常使用．

## Author

👤 **MikoAI**

* Twitter: [@https://www.twitter.com/miko69877984](https://twitter.com/https://www.twitter.com/miko69877984)
* Github: [@MikoSecSoS](https://github.com/MikoSecSoS)

## 🤝 Contributing

Contributions, issues and feature requests are welcome !<br />Feel free to check [issues page](https://github.com/MikoSecSoS/GetURLs/issues).

## Show your support

Give a ⭐️ if this project helped you !

## 📝 License

Copyright © 2019 [MikoAI](https://github.com/MikoSecSoS).<br />
This project is [MIT](https://github.com/MikoSecSoS/readme-md-generator/blob/master/LICENSE) licensed.

***
_This README was generated with ❤️ by [readme-md-generator](https://github.com/kefranabg/readme-md-generator)_
