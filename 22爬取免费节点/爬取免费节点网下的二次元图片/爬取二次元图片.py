# -*-coding:utf8-*-
import os,sys
import re
import json
import time
from urllib import response
import bs4
import pandas 
import urllib 
import requests
from fake_useragent import UserAgent #随机请求头库
from selenium import webdriver # 模拟用户操作
from msedge.selenium_tools import EdgeOptions  # 用于selenium无界面
from msedge.selenium_tools import Edge
from urllib import request  # 用于重定向
from colorama import Fore # 调色
from collections import Counter  # 用于统计
from prettytable import PrettyTable  # 美化表格的包
from pyquery import PyQuery as pq  # 解析 DOM 节点的结构
from pathlib import Path
os.chdir(sys.path[0]) # 加上即可使用相对路径(解决相对路径问题)
# os.chdir() 方法用于改变当前工作目录到指定的路径。path-要切换到的新路径。


base_url = 'https://freenode.me/f/freenode/page/1'

headers = {
    'User-Agent': UserAgent().random
}
response = requests.get(base_url)
with open(file="img.html", mode="w", encoding="utf-8")as f:
    f.write(response.text)
    f.close()
