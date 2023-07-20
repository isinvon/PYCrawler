# -*-coding:utf8-*-
import json
import os
import re
from struct import pack
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
from selenium import webdriver  # 模拟用户操作

os.chdir(sys.path[0])  # 加上即可使用相对路径(解决相对路径问题)
# os.chdir() 方法用于改变当前工作目录到指定的路径。path-要切换到的新路径。


str = '2021469084@qq.com'

result = re.findall('2021469084@qq\.com', str)
print(result)
