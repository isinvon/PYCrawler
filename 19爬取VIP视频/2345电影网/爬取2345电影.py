# -*-coding:utf8-*-
import json
import os
import re
import sys
import time
import urllib
from collections import Counter  # 用于统计
from pathlib import Path
from urllib import request  # 用于重定向

import bs4
import pandas
import requests
from colorama import Fore  # 调色
from fake_useragent import UserAgent  # 随机请求头库
from msedge.selenium_tools import EdgeOptions  # 用于selenium无界面
from msedge.selenium_tools import Edge
from prettytable import PrettyTable  # 美化表格的包
from pyquery import PyQuery as pq  # 解析 DOM 节点的结构
from selenium import webdriver  # 模拟用户操作

os.chdir(sys.path[0])  # 加上即可使用相对路径(解决相对路径问题)
# os.chdir() 方法用于改变当前工作目录到指定的路径。path-要切换到的新路径。

# url1 = 'https://dianying.2345.com/'
url = 'https://kan.2345.com/'
header = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'Accept-Language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    'Cookie': 'uUiD=7314216846478877508908; lc2=59431; lc=59431; wc=59431; wc_n=%25u5357%25u5B81%25u5E02; HTTP_FOR_REFERER=https%3A%2F%2Fwww.2345.com%2F; HTTP_REFERER=www.2345.com; YSRF=index',
    'Host': 'dianying.2345.com',
    'If-Modified-Since': 'Sun, 21 May 2023 16:20:03 GMT',
    'If-None-Match': 'W/"646a44b3-6dad6"',
    'Referer': 'https://www.2345.com/',
    'sec-ch-ua': '"Microsoft Edge";v="113", "Chromium";v="113", "Not-A.Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'same-site',
    'Sec-Fetch-User': '?1',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': UserAgent().random,
}


def get_html():
    response = requests.get(url)
    response.encoding = response.apparent_encoding
    html = response.text
    soup = bs4.BeautifulSoup(html, 'lxml')
    print(soup.prettify())


if __name__ == '__main__':
    get_html()
