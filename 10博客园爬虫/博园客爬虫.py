# -*-coding:utf8-*-
import os
import sys
import re
import json
import time
from unittest import result
import bs4
from h11 import Data
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
from pathlib import Path

os.chdir(sys.path[0])  # 加上即可使用相对路径(解决相对路径问题)
# os.chdir() 方法用于改变当前工作目录到指定的路径。path-要切换到的新路径。


# 全局变量
headers = {
    "content-type": "application/json; charset=UTF-8",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36",
    "cookie": "__gads=ID=85ea91454ff7ae2a:T=1661687799:S=ALNI_MZ65JoXR05zq1W3T-VaRRv2ZNt33A; _clck=t1351q|1|f8y|0; _ga_3Q0DVSGN10=GS1.1.1676447541.2.1.1676447564.37.0.0; _ga=GA1.2.486211484.1655131579; Hm_lvt_32247700466dcd5fcde2763a97d5c0e3=1677086777; .AspNetCore.Antiforgery.b8-pDmTq1XM=CfDJ8M-opqJn5c1MsCC_BxLIULkEBrkZ-GWjgWHK5gU5qbIsF9CDZy_nOH99Yu6wo8tEhqf9tv0LNVm8fYeICfVCCGiWo1CKZjR7MB9CpLob-dH7B2CTPDt_ooNNCQh5SvN9kMM9RtxDVPxMEArFsY7kRW4; cto_bundle=T37qz19aJTJCdEJkWHolMkZ6cEZXQXNPbnNKaE5Vdmp6U080OVZCeG9HZGJ5a01kT3dCZk5xTTMlMkJvQlhqNUhWU1VlT1cxJTJCQ3cxeDZJV2t0WWdwS2twWkVEbWpDN0c0UUZGcWR5UVR1UFRGODElMkZPUkhObkFlZlNZazZ5c1BHTUolMkJOcTFkb1JlMm1pc0xFeG5OaU9uZjhIQyUyQnElMkI5U0RnJTNEJTNE; Hm_lvt_866c9be12d4a814454792b1fd0fed295=1680092546; _gid=GA1.2.1407189783.1681206623; _gat_gtag_UA_476124_1=1; __gpi=UID=0000092d001786a0:T=1661687799:RT=1681206624:S=ALNI_MZPIJqiVbfHw8A7v5uOjGsLCfq4fA; Hm_lpvt_866c9be12d4a814454792b1fd0fed295=1681206665",
}
basic_url = "https://www.cnblogs.com/#p{}"

'''
    :param page_start: 页码
    :param page_end: 页码
    :return:
'''


def get_info(page_start, page_end):
    if page_start > 0:
        pass
    else:
        print("输入的页码不正确")
        exit(0)
    data = []
    all_data = []  # 字典
    for i in range(page_start, page_end + 1):  # 循环页数
        url = basic_url.format(str(i))  # 补全url
        # print("=============================================================" + url)  # 当前url
        response = requests.get(url=url, headers=headers)
        content = response.text
        html = content
        soup = bs4.BeautifulSoup(html, 'lxml')
        for num in range(1, 20):
            article = soup.select("article[class='post-item']")[num]
            text = soup.select("div[class='post-item-text']")[num]
            title = text.select("a[class='post-item-title']")[0].text
            link = text.select("a[class='post-item-title']")[0].get("href")
            footer = article.select("footer[class='post-item-foot']")  # 每一章的脚
            author = footer[0].select("a span")[0].text  # 作者
            like = footer[0].select("a span")[1].text  # 喜欢
            comment = footer[0].select("a span")[2].text  # 评论
            look = footer[0].select("a span")[3].text  # 观看
            print(Fore.WHITE + str(title) + "\n"
                  + "   点赞:" + like + " 评论:" + comment + "观看:" + look + " 作者:" + author + "\n"
                  + Fore.GREEN + "   {}=> ".format(num) + link + "\n"
                  + "--------------------------")
            data.append([title, like, comment, look, author, link])
    return data



if __name__ == '__main__':
    # 得到起始页码
    page_start = 1
    page_end = 1
    all_data = get_info(page_start=page_start, page_end=page_end)
    df = pandas.DataFrame(
        all_data, columns=['标题', '点赞', '评论', '观看', '作者', '链接'])
    df.to_excel("博园客文章信息.xlsx", index=False)
