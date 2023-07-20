# -*-coding:utf8-*-
from ast import pattern
from itertools import count
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
os.chdir(sys.path[0])  # 加上即可使用相对路径(解决相对路径问题)
# os.chdir() 方法用于改变当前工作目录到指定的路径。path-要切换到的新路径。


class Img():

    base_url = 'https://freenode.me/f/freenode/page/'
    headers = {
        'User-Agent': UserAgent().random
    }

    # 计数
    def count(self):
        count = self.Count + 1
        return count

    # 单个网页
    def get_html(self, page):
        response = requests.get(self.base_url+str(page))
        with open(file="img.html", mode="w", encoding="utf-8")as f:
            f.write(response.text)
            f.close()

    # 单个网页的图片
    def get_img(self, count):
        with open(file="img.html", mode="r", encoding="utf-8")as f:
            html = f.read()
            f.close()
        img_list = []
        # 图片序号命名
        
        soup = bs4.BeautifulSoup(html, "lxml")
        img_tag = soup.select("span img[class='thumbnail']")
        length = len(img_tag)
        for i in range(0, length):
            img_tag = soup.select("span img[class='thumbnail']")[
                i].attrs.get("data-original")
            img_list.append(img_tag)
        length = len(img_list)

        for i in range(0, length):
            # 返回字节流
            imgByte = requests.get(img_list[i]).content
            # 计算图片的序号
            if not os.path.exists('图片'):
                os.makedirs('图片')
            try:
                with open('图片/{}.jpg'.format(str(count)), 'wb') as f:
                    f.write(imgByte)
                    print('{}.jpg-----下载成功'.format(str(count)))
            except:
                print(f'{str(count)}.jpg下载失败！')
            count = count + 1

    def main(self, page, count):
        self.get_html(page)
        self.get_img(count)


if __name__ == '__main__':
    img = Img()
    count = 0
    page = int(input('请输入末尾页数: '))
    if 0 < page < 20:
        for i in range(1, page+1):
            img.main(page, count)
            count = count + 1
    else:
        print("页数得在[1,20]之间")
