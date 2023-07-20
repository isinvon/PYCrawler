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
from selenium import webdriver  # 模拟用户操作

os.chdir(sys.path[0])  # 加上即可使用相对路径(解决相对路径问题)


# os.chdir() 方法用于改变当前工作目录到指定的路径。path-要切换到的新路径。


def get_data():
    data = []
    url = 'https://creator.douyin.com/aweme/v1/creator/data/billboard/?billboard_type=9'
    response = requests.get(url)
    html = response.text
    soup = bs4.BeautifulSoup(html, 'lxml').select('p')[0]
    text = soup.text
    lenght = len(re.findall('"title":"(.*?)"}', string=text))  # 732
    for i in range(0, 500 + 1):  # 取500条
        title = re.findall('"title":"(.*?)"}', text)[i]
        img_link = re.findall('"img_url":"(.*?)"', text)[i]
        link = re.findall('"link":"(.*?)"', text)[i]
        data.append([title, link, img_link])
    print('列表生成完毕...')
    return data


def create_csv(data):  # 转为CSV
    dataForm = pandas.DataFrame(data=data, columns=['title', 'link', 'image'])
    dataForm.to_csv('抖音上升榜.csv', index=False)
    print('CSV表格已生成...')


def create_excel(data):  # 转为EXCEL
    dataForm = pandas.DataFrame(data=data, columns=['title', 'link', 'image'])
    dataForm.to_excel('抖音上升榜.xlsx', index=False)
    print('EXCEL表格已生成...')


if __name__ == '__main__':
    data = get_data()
    # 转为CSV
    # create_csv(data)
    # 转为Excel
    create_excel(data)
