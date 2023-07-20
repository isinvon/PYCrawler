# -*-coding:utf-8 -*-
import pymysql
import requests
import os
from lxml import etree
from fake_useragent import UserAgent
import sqlite3
# -*-coding:utf8-*-
import os, sys

os.chdir(sys.path[0])  # 加上即可使用相对路径(解决相对路径问题)


# os.chdir() 方法用于改变当前工作目录到指定的路径。path-要切换到的新路径。


# 教程: https://www.52pojie.cn/thread-1450685-1-1.html

def RquestTools(url):
    headers = {
        'User-Agents': str(UserAgent().random)
    }  # 设置请示头部数据,防止被反爬虫面爬不到数据
    response = requests.get(url, headers=headers)  # get一下url网址
    response.encoding = response.apparent_encoding  # 最终的解码方式,全程解码错误,因为有方式1和2到同样一个页面都会编码错误,最后请教别人使用这个方法,已经成功爬完所有的数据
    response = response.text  # 提取get回来的text数据(text是Beautifulsoup根据猜测的编码方式将content内容编码成字符串。)
    # response = requests.tet(url,headers=headers).content.decode('bgk') #解码方式1,有错误,爬到一千多面的时候有一个页面会编码错误
    # response = response.encode('raw_unicode_escape').decode('gbk')#解码方式2,有错误,跟解码方式1一样,爬到同样位置会出错
    # response = response.encode('ISO-8859-1') #response = response.decode('gbk')  #解码方式3,有错误
    response = etree.HTML(response)
    return response


def str_finishing(seif):  # sqlite3字符处理，因为有些符号影响sqlite命令行，所以需要处理
    str_temp = seif
    str = str_temp.replace("/", "//")
    str = str.replace("\'", "''")
    str = str.replace("[", "/[")
    str = str.replace("]", "/]")
    str = str.replace("%", "/%")
    str = str.replace("_", "/_")
    str = str.replace("(", "/(")
    str = str.replace(")", "/)")
    return str


url = 'http://www.world68.com/country.asp'  # 设置请求网址
html = RquestTools(url)  # 获取第一层url的THML信息(为了提取国家名称及对应的url地址)
country = html.xpath('//div[@class="content_all r"]/dl/dd/a[1]/text()')  # xpath定位国家名称
country_url = html.xpath('//div[@class="content_all r"]/dl/dd/a[1]/@href')  # xpath定位国家url地址
conn = sqlite3.connect("worldurl.db")  # 获取或创建数据库链接
# conn = pymysql.connect("worldurl.sql")  # 获取或创建数据库链接
litec = conn.cursor()  # 获取游标

for i, c in zip(country, country_url):
    sqltable = 'create table ' + i + '(urltype,urlname,urladdress,urlintroduce)'  # 设置sqlite3的脚本语句,意思为 [创建-表格-表格名称(列)]
    litec.execute(str(sqltable))  # 执行sqlite3的脚本[sqltable = 创建-表格-国家-(网站分类-网站名称-网站地址-网站简介)],增加表格这些是不需要提交修改事务的,这里的修改会直接出现在db文件里
    corntry_html = RquestTools(c)  # 获取第二层url的HTML信息(为了提取网站类型及对应链接)
    cont_r_sort_c = corntry_html.xpath('//div[@class="content_r_sort_c"]/ul/li/a/text()')  # xpath定位网站分类
    cont_r_sort_c_url = corntry_html.xpath('//div[@class="content_r_sort_c"]/ul/li/a/@href')  # xpath定位网站分类url地址
    for v, m in zip(cont_r_sort_c, cont_r_sort_c_url):
        tryhtml = RquestTools(m)  # 获取第三层url的HTML信息(为了提取网站名称对应的Url地址,用此来提取第四层信息)
        urls = tryhtml.xpath('//dl[@class="top_page"]/dt/a/@href')
        for ii in urls:
            tryhtm2 = RquestTools(ii)  # 获取第四层url的HTML信息(为了提取网站名称\网站地址\网站简介)
            country_name = "".join(tryhtm2.xpath('//div[@class="name_r r"]/a/text()'))  # 网站名称
            country_name = str_finishing(country_name)  # 其中可能包含sqlite3的需要处理的符号,所以通过str_finishing处理一下
            country_url = "".join(tryhtm2.xpath('//div[@class="name_r r"]/a/@href'))  # 网站地址 #网站Url地址内没有需要处理的符号,所以直接就用了
            country_lits = "".join(tryhtm2.xpath('//div[@class="jianjie_r r"]/p/text()'))  # 网站简介
            country_lits = str_finishing(country_lits)  # 其中可能包含sqlite3的需要处理的符号,所以通过str_finishing处理一下
            sqladd = 'insert into ' + i + ' values (\'' + v + '\',\'' + country_name + '\',\'' + country_url + '\',\'' + country_lits + '\')'
            litec.execute(str(sqladd))  # 执行sqlite3的脚本,[新增-国家-(网站分类-网站名称-网站地址-网站简介)]
        conn.commit()  # 提交修改事务,新增数据是需要提交修改的,所以在这里加这条,是为了增加了条一种不同的网站类别的数据后(也就是第四层HTML信息)提交一次
# 关闭资料,sqlite3 打开了需要关闭,先关游标,再关文件,所有的python中open的文件都是需要关闭的,不然会出错
litec.close()  # 这里是关闭游标
conn.close()  # 这里是关闭数据库
