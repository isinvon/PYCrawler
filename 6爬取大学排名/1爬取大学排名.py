# -*-coding:utf8-*-
import os,sys
import re
import json
import time
import bs4
import pandas
import requests
from fake_useragent import UserAgent #随机请求头库
from selenium import webdriver
from msedge.selenium_tools import EdgeOptions  # 用于selenium无界面
from msedge.selenium_tools import Edge
from urllib import request  # 用于重定向
from colorama import Fore
import urllib 
from collections import Counter  # 用于统计
from prettytable import PrettyTable  # 美化表格的包
from pathlib import Path
os.chdir(sys.path[0]) # 加上即可使用相对路径(解决相对路径问题)
# os.chdir() 方法用于改变当前工作目录到指定的路径。path-要切换到的新路径。

# 从网络上获取大学排名网页内容。
def getHTMLText(url):  # 获取URL信息，输出内容
    # =========================方式1获取=========================
    try:
        res = requests.get(url)  # 使用requests库爬取
        res.raise_for_status()  # 产生异常信息
        res.encoding = res.apparent_encoding  # 修改编码
        return res.text  # 返回网页编码
    except Exception as err:
        print(err)

    # =========================方式2获取=========================
    try:
        req = urllib.request.Request(url)
        # 打开URL网站的网址，读出二进制数据，二进制数据转为字符串
        data = urllib.request.urlopen(req).read.decode()
        return data
    except Exception as err:
        print(err)
# 提取网页内容中信息到合适的数据结构.
def fillUnivList(ulist, html):  # 将html页面放到ulist列表中(核心)
    # 解析网页文件（使用html解释器）
    soup = bs4.BeautifulSoup(html, "html.parser")
    # soup.prettify()  # 把soup对象的文档树变换成一个字符串
    # 数据结构:所用数据都封装在一个表格(标签tbody)中，单个学校信息在tr标签中，详细信息在td标签中
    # 学校名称在a标签中，定义一个列表单独存放a标签内容
    for tr in soup.find('tbody').children:
        if isinstance(tr, bs4.element.Tag):  # 如果tr标签的类型不是bs4库中定义的tag类型，则过滤掉
            a = tr('a')  # 把所用的a标签存为一个列表类型
            tds = tr('td')  # 将所有的td标签存为一个列表类型
            ulist.append([tds[0].text.strip(), a[0].string.strip(), tds[2].text.strip(),
                          tds[3].text.strip(), tds[4].text.strip()])
            # 使用strip()函数，它的作用是用于移除字符串头尾指定的字符（默认为空格或换行符）或字符序列

# 利用数据结构展示并输出结果:定义函数
def printUnivList(ulist1, num):  # 打印出ulist列表的信息，num表示希望将列表中的多少个元素打印出来
    # 格式化输出
    tplt = "{0:^10}\t{1:^10}\t{2:^12}\t{3:^12}\t{4:^10}"
    print(tplt.format("排名", "学校名称", "省份", "学校类型", "总分"))
    for i in range(num):
        u = ulist1[i]
        print(tplt.format(u[0], u[1], u[2], u[3], u[4]))




def main():
    uinfo = []  # 将大学信息放到列表中
    url = "https://www.shanghairanking.cn/rankings/bcur/2020"
    html = getHTMLText(url)
    fillUnivList(uinfo, html)
    printUnivList(uinfo, 30)  # 一个界面的数据


if __name__ == '__main__':
    main()
