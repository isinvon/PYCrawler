# -*-coding:utf8-*-
import os
import sys
import re
import json
import time
import bs4
import pandas
import urllib
import requests
from fake_useragent import UserAgent  # 随机请求头库
from selenium import webdriver  # 模拟用户操作
from msedge.selenium_tools import EdgeOptions  # 用于selenium无界面
from msedge.selenium_tools import Edge
from urllib import request  # 用于重定向
from colorama import Fore  # 调色
from collections import Counter  # 用于统计
from prettytable import PrettyTable  # 美化表格的包
from pyquery import PyQuery as pq  # 解析 DOM 节点的结构
from pathlib import Path

url = 'https://dh.aabyss.cn/'


def get_res():
    res = requests.get(url)
    text = res.text
    with open(file="website.html", mode="w", encoding="utf-8") as f:
        f.write(text)
        f.close()
    with open(file="website.html", mode="r", encoding="utf-8") as f:
        text = f.read()
        f.close()
    soup = bs4.BeautifulSoup(text, 'lxml')
    # 定义数组
    tag_list = []
    # 获取网站数量
    length = len(soup.select('div[class="col-sm-3"]'))
    for i in range(0, length):
        # 主标签
        tag_main = soup.select('div[class="col-sm-3"]')[i]
        # 名字
        tag_name = tag_main.select(
            'a[class="xe-user-name overflowClip_1"]')[0].text.strip()
        # 链接
        tag_link = tag_main.select('div')[0].attrs.get(
            'data-original-title').strip()
        # 图标
        if tag_main.select('img')[0].attrs.get('src').strip().replace(' ', '').__contains__('http'):
            tag_image = tag_main.select('img')[0].attrs.get(
                'src').strip().replace(' ', '')
        else:
            tag_image = 'https://dh.aabyss.cn' + \
                tag_main.select('img')[0].attrs.get(
                    'src').strip().replace(' ', '')
        # 描述
        tag_description = tag_main.select('p')[0].text.strip()
        print("--------------------------------------------------")
        print(tag_name + '\n' + tag_link + '\n' +
              tag_image + '\n' + tag_description)

        # 将标签信息组装成一个字典
        tag_info = {
            'name': tag_name,
            'link': tag_link,
            'image': tag_image,
            'description': tag_description
        }
    
        
        # 将字典添加到标 json_data = json.dumps(tag_list, ensure_ascii=False, indent=2)签列表中
        tag_list.append(tag_info)
    # 将标签列表转换为 JSON 格式
    # 将 JSON 数据保存到文件中，比如 "tags.json"
    with open('website.json', 'w', encoding='utf-8') as file:
        file.write(tag_list)


if __name__ == '__main__':
    get_res()
