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
import openpyxl
import pandas
import requests
import xlrd  # 查询Excel表
from colorama import Fore  # 调色
from fake_useragent import UserAgent  # 随机请求头库
from msedge.selenium_tools import EdgeOptions  # 用于selenium无界面
from msedge.selenium_tools import Edge
from prettytable import PrettyTable  # 美化表格的包
from pyquery import PyQuery as pq  # 解析 DOM 节点的结构
from selenium import webdriver  # 模拟用户操作

os.chdir(sys.path[0])  # 加上即可使用相对路径(解决相对路径问题)
# os.chdir() 方法用于改变当前工作目录到指定的路径。path-要切换到的新路径。

url = 'https://tools.2345.com/yb.htm'
headers = {
    'User-Agent': UserAgent().random,
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    'Host': 'tools.2345.com',
    'Referer': 'https//www.baidu.com/link?url=etnNT2iKSmRHdOnA08YPNHJk_ZSZCrBJD2p322fMLW13yrGHKSiAG6jGeRFueXhm&wd=&eqid=ff3f3aed000123150000000664698e93',
    'Upgrade-Insecure-Requests': '1',
}


def get_postCode_html():
    response = requests.get(url=url, headers=headers)
    response.encoding = response.apparent_encoding
    html = response.text
    doc = pq(html)  # 这样就能使用jquery来修改html元素了

    # 因为2345的网页将某些地区的编码设置style="display:none"(隐藏标签),所以需要修改属性才能查看"https://blog.csdn.net/hou9876543210/article/details/105881759"
    if doc('.rendData').attr:
        # attr()放一个元素是获取值,两个元素的时候是修改
        doc('.rendData').attr('style', "display: block")
        # 参考pyquery的使用方法:"https://blog.csdn.net/weixin_43670190/article/details/106493948"
        response = requests.get(url=url, headers=headers)  # 修改后继续访问
        response.encoding = response.apparent_encoding
        new_html = response.text  # 得到修改属性之后的新标签
        return new_html
    else:
        print("无法获取本页面内容")


def get_data(html):
    # 用于存储所有区的列表
    data = []
    soup = bs4.BeautifulSoup(html, 'lxml')
    # 获取所有省份的html(列表类型)
    convences = soup.select('div[class="rendData"]')
    for convence in convences:  # 迭代省份
        tr = convence.select('tbody tr')  # index[1]为该省份的第一个城市
        tr_len = len(tr) - 1  # 每个省份的 区/县 数量
        # 定义一个累积量
        num = 0
        for tr_single in tr:
            if num == 0:
                pass  # 排除表格第一行的无关信息: 类似于名称啥的
            else:
                # 得到区的标签
                td = tr_single.select('td')
                # 区标签的长度
                td_len = len(td)
                # 开始进行判断:
                '''
                特殊情况:判断每个tr下是否是6个或者3个td标签
                        1. 如果大于3, 小于6就只要tr里的前三个td标签
                        2. 如果等于6,可以取完所有td标签
                        3. 如果大于6则不考虑
                        
                '''
                if 3 <= td_len < 6:
                    try:
                        # 分别是: (市、县、区名),(长途区号),(邮政编码)
                        data.append([str(td[0].text), str(
                            td[1].text), str(td[2].text)])
                    except:
                        print("---异常区可供参考的参数---")
                        print("tr_len: ", tr_len)
                        print("num: ", num)
                        print("td_len: ", td_len)
                        print(
                            f'[str(td[0].text): {str(td[0].text)}, str(td[1].text): {str(td[1].text)}, str(td[2].text)]: {str(td[2].text)}')
                elif td_len == 6:
                    data.append([str(td[0].text), str(
                        td[1].text), str(td[2].text)])
                    data.append([str(td[3].text), str(
                        td[4].text), str(td[5].text)])
                else:
                    pass
            num += 1  # 第一次累加以后会一直大于1, 后面的列表得以存入列表data[]中
    return data


def print_table(data):
    table = PrettyTable(['市、县、区名', '长途区号', '邮政编码'])
    table.add_rows(data)
    print(table)


def create_csv(data):  # 转为CSV
    dataForm = pandas.DataFrame(data=data, columns=['市、县、区名', '长途区号', '邮政编码'])
    dataForm.to_csv('城市编码.csv', index=False)
    print('CSV表格已生成...')
    print('==================')


def create_excel(data):  # 转为EXCEL
    dataForm = pandas.DataFrame(data=data, columns=['市、县、区名', '长途区号', '邮政编码'])
    dataForm.to_excel('城市编码.xlsx', index=False)
    print('EXCEL表格已生成...')
    print('==================')


def search_cityPostCode_by_city_by_excel():  # 查询某市的编码(从Excel)
    # pandas的模糊查询'https://www.cnblogs.com/cxyrj/p/12861897.html'
    # 其他教程: 'https://blog.csdn.net/weixin_45082522/article/details/106364847'
    for i in range(0, 100000):
        city = str(input("请输入城市: "))
        '''
        非模糊查询:
        for name in data:
            if city in name:
                zx_lists.append(name)
        print(zx_lists)
        '''
        # 非模糊查询方法2:
        excel_file = '城市编码.xlsx'  # 导入excel数据
        data = pandas.read_excel(excel_file, index_col='市、县、区名')
        # 这个的index_col就是index，可以选择任意字段作为索引index，读入数据
        str1 = data.loc[city]
        print(str1)




if __name__ == '__main__':
    html = get_postCode_html()  # 得到html
    data = get_data(html)  # 得到数据列表
    print_table(data)  # 控制台打印漂亮的表格
    create_excel(data)  # 生成excel表格
    search_cityPostCode_by_city_by_excel()  # 根据城市名字查询
