# -*-coding:utf8-*-
import html
import os
import re
import sys
from urllib import request  # 用于重定向

import requests
import wget  # 下载
from colorama import Fore  # 调色
from fake_useragent import UserAgent  # 随机请求头库
from prettytable import PrettyTable  # 美化表格的包

# 定位到当前父目录下
os.chdir(sys.path[0])  # 加上即可使用相对路径(解决相对路径问题)
# os.chdir() 方法用于改变当前工作目录到指定的路径。path-要切换到的新路径。


url = 'https://freenode.me/f/freenode'


def get_url():
    headers = {
        'referer': 'https://freenode.me/',
        # 欺骗
        'User-agent': UserAgent().random
    }
    response = requests.get(url=url, headers=headers)
    if response.status_code == 200:
        response.encoding = response.apparent_encoding
        html = response.text
        # soup = bs4.BeautifulSoup(html, 'lxml')
        vpnNumLists = re.findall(
            'https\:\/\/freenode\.me\/a\/(.*?)\.html', html)
        # str字符列表转化为int列表
        vpnNumLists1 = list(map(int, vpnNumLists))
        # 降序排序
        vpnNumLists1.sort(reverse=True)
        # 再将int转化为str
        vpnNumLists2 = list(map(str, vpnNumLists1))
        # 取最大的数字来拼接vpn的url
        vpnUrl = f'https://freenode.me/a/{vpnNumLists2[0]}.html'
        # 返回url
        return vpnUrl
    else:
        print(url, '无法访问')
        exit(0)  # 终止程序


# 进行访问且下载该文件

def get_yamlFile(vpn_url):
    headers = {
        'User-agent': UserAgent().random,
    }
    response = requests.get(url=vpn_url, headers=headers)
    if response.status_code == 200:
        response.encoding = response.apparent_encoding
        html = response.text
        # 得到url
        vpnTXT = re.findall(
            'https://freenode.me/wp-content/.*?.txt', html)[0].strip()
        vpnYaml = vpnTXT.replace('txt', 'yaml')
        # 得到文件日期
        vpmDate = vpnTXT.split(
            '/uploads/')[1].split('.txt')[0].replace('/', '.')
        # 输出方案
        print(Fore.GREEN + '---------------------------------------------------------------------')
        print(Fore.LIGHTWHITE_EX + 'v2ray&小火箭：', vpnTXT)
        print(Fore.LIGHTBLUE_EX + 'Clash&小火箭：', vpnYaml)
        print(Fore.GREEN + '---------------------------------------------------------------------')

        # 如果出现:HTTPError: Forbidden, 其实加一个请求头或者更多的参数即可
        opener = request.build_opener()  # urllib.request中的hearders要通过创建opener实现
        opener.addheaders = [('User-Agent',
                              UserAgent().random)
                             ]
        request.install_opener(opener)
        # 创建一个文件夹,装两个vpn文件
        if os.path.exists('节点文件'):
            pass
        else:
            os.mkdir('节点文件')
        # urlretrieve不会判断文件夹存在与否,需独自创建
        request.urlretrieve(
            url=vpnTXT, filename=f'./节点文件/vpnTXT({vpmDate}).txt')
        request.urlretrieve(
            url=vpnYaml, filename=f'./节点文件/vpnYaml({vpmDate}).yaml')
        print(
            Fore.WHITE + f'vpnTXT({vpmDate}).txt是[v2ray]专用' + '\n' + 'vpnYaml({vpmDate}).yaml是[Clash]专用')
        print(Fore.CYAN + '下载完成...')
        # wget法 下载文件
        # eg: wget.download(vpnYaml, 'vpnTXT.yaml')


if __name__ == '__main__':
    urlLasted = get_url()
    get_yamlFile(urlLasted)
