# 3.05 bnq:/ 这大概就是学吉他的意义了吧# 一万次悲伤 # 吉他弹唱 # 牛丁吉他2
# https://v.douyin.com/DXn8k26/ 复制此链接，打开Dou音搜索，直接观看视频！
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

os.chdir(sys.path[0]) # 加上即可使用相对路径(解决相对路径问题)
# os.chdir() 方法用于改变当前工作目录到指定的路径。path-要切换到的新路径。
'''
提供条件: 给出一个抖音视频的url
需求:
    视频标题
    视频本身mp4格式下载到本地(声音和视频或者有声视频)
    作者名称    
    作者的主页url
    头像(jpg格式下载到"头像文件夹中")
    作者的性别,抖音号,IP地址,大学
    作者的粉丝数,获赞总数
    主页简介(可选)
    作者主页前三个有"置顶"字样的视频的名字的点赞数
教程提供: 
    爬取用户具体信息: https://zhuanlan.zhihu.com/p/141771075   # (知乎教程_重点参考)
                    https://www.cnblogs.com/songzhixue/articles/11241502.html
                    https://www.lydingpin.com/gonglue/114370710.html
                    http://element-ui.cn/article/show-257928.aspx?action=onClick  ->需要使用fiddler抓包工具
                    https://blog.csdn.net/weixin_39699313/article/details/110330784
                    https://www.cnblogs.com/zeifenbing/articles/16272147.html  (重量级)
'''

def get_info1(url, headers):  # 返回作者主页的url
    response = requests.get(url=url, headers=headers)
    if response.status_code == 200:
        response.encoding = response.apparent_encoding  # 赋予解码方式
        html = response.text  # 视频藏在html中,需要解密
        # ①视频的标题
        title = re.findall('<title data-react-helmet="true">(.*)</title>', html)[0]
        # 源码转为bs4类型
        soup = bs4.BeautifulSoup(html, 'lxml')
        # 找到作者主页所在的标签,并且取标签中的文本
        home_page = soup.select('script')[11].text  # 文本格式的json
        # 转成json格式
        home_page = json.loads(home_page)  # home_page的内容查看->home_page_json_demo.txt
        # ②作者名字
        author_name = home_page["itemListElement"][1]["name"]
        # ③作者的主页url
        author_home_page = home_page["itemListElement"][1]["item"]

        # ④视频mp4格式资源下载
        #       相关拓展: 操控控制台法--> https://zhuanlan.zhihu.com/p/496076747

        # 单纯声音的资源-----------------------------------------------------
        # 正则匹配到音频的参数串
        audio_source = re.findall("v26.*?.btag.*?.%", html)[2]
        # 切片法去掉最后一个字符%,切片法教程: https://blog.csdn.net/weixin_35753431/article/details/129062194
        audio_source = audio_source[:len(audio_source) - 1]
        # 加上https://就是mp4视频的完整url
        audio_source = "https://" + audio_source
        # url解码(不解码无法访问)(密文转化为人看得懂的),urllib.parse.unquote(),教程: https://blog.csdn.net/smallfox233/article/details/107993222
        audio_source = urllib.parse.unquote(audio_source)
        # 结果eg: https://v26-web.douyinvod.com/dee8bbb34bda6fb7c162ad5bb13766b8/6452b3b1/video/tos/cn/tos-cn-ve-15c001-alinc2/oM6OAubnDhG196kAAeKcIFAHoB2AXDOB8AeyRg/?a=6383&ch=26&cr=3&dr=0&lr=all&cd=0%7C0%7C0%7C3&cv=1&br=741&bt=741&cs=2&ds=6&ft=7yV4ZBo7UUmfAcdFO02D1YswHAX1tGQP9Aq9eFGMcvQr12nz&mime_type=video_mp4&qs=11&rc=ZDU0aWQ1NjhnM2Q4ZzkzNEBpajNoMzQ6ZmY6ajMzNGkzM0A2YF4xMjYtXjExYTYxYTJiYSMwcXFkcjRnNF5gLS1kLTBzcw%3D%3D&l=202305040216277C82D9FD70E03C982651&btag=e00028000

        # 视频(有声)资源------------------------------------------------------
        # 正则匹配到视频的参数串
        video_source = re.findall("v3-web.douyinvod.com.*?.btag.*?.%", html)[2]
        # 切片法去掉最后一个字符%,切片法教程: https://blog.csdn.net/weixin_35753431/article/details/129062194
        video_source = video_source[:len(video_source) - 1]
        # 加上https://就是mp4视频的完整url
        video_source = "https://" + video_source
        # url解码(不解码无法访问)(密文转化为人看得懂的),urllib.parse.unquote(),教程: https://blog.csdn.net/smallfox233/article/details/107993222
        video_source = urllib.parse.unquote(video_source)
        # 结果eg: https://v3-web.douyinvod.com/fe0edb2642bcd2a3ce781d0d423e4e66/6452b383/video/tos/cn/tos-cn-ve-15c001-alinc2/o8HBC6yb4r4k8AAGhOOc9AAngDfADXFOAuFSRf/?a=6383&ch=26&cr=3&dr=0&lr=all&cd=0%7C0%7C0%7C3&cv=1&br=3987&bt=3987&cs=0&ds=4&ft=7yV4ZBo7UUmfAcdFO02D1YswHAX1tGLP9Aq9eFGMcvQr12nz&mime_type=video_mp4&qs=0&rc=OjlmZDg1OTloaWY6MzppOEBpajNoMzQ6ZmY6ajMzNGkzM0AyMWExYC8uXjMxNF9eNi4uYSMwcXFkcjRnNF5gLS1kLTBzcw%3D%3D&l=20230504021542A86B49EA6117F4A55E11&btag=e00028000
        '''
        上面得到信息: v26-web.douyinvod.com%2Fd703a86a1add3fd65c8aacd88727eebf%2F6452add3%2Fvideo%2Ftos%2Fcn%2Ftos-cn-ve-15c001-alinc2%2FoM6OAubnDhG196kAAeKcIFAHoB2AXDOB8AeyRg%2F%3Fa%3D6383%26ch%3D26%26cr%3D3%26dr%3D0%26lr%3Dall%26cd%3D0%257C0%257C0%257C3%26cv%3D1%26br%3D741%26bt%3D741%26cs%3D2%26ds%3D6%26ft%3D7yV4ZBo7UUmfAcdFO02D1YswHAX1tGT9kAq9eFGMcvQr12nz%26mime_type%3Dvideo_mp4%26qs%3D11%26rc%3DZDU0aWQ1NjhnM2Q4ZzkzNEBpajNoMzQ6ZmY6ajMzNGkzM0A2YF4xMjYtXjExYTYxYTJiYSMwcXFkcjRnNF5gLS1kLTBzcw%253D%253D%26l%3D2023050401512688F47CC39D7C87C45A5B%26btag%3De00028000%
        最后一个参数为btag,记得去掉最后的那个%才是mp4完整路径
        '''
        print('-----------------------------------------------')
        print("作品: ", title, '\n链接: ', url, '\n视频下载: ', video_source, '\n音频下载: ', audio_source, "\n作者: ", author_name,
              "\n主页: ", author_home_page, )
        print(Fore.LIGHTWHITE_EX + '-----------------------------------------------')

        return author_home_page  # 主页url
    else:
        print(Fore.LIGHTRED_EX + '抖音链接无法访问...')


def get_info2(author_home_page):
    # 模拟浏览器访问作者主页
    response = requests.get(url=author_home_page, headers=headers)
    response.encoding = response.apparent_encoding
    html = response.text
    soup = bs4.BeautifulSoup(html, 'lxml')
    # ⑤获取关注数,粉丝数,获赞数
    follow_all = soup.select('div[class="TxoC9G6_"]')[0].text
    fans_all = soup.select('div[class="TxoC9G6_"]')[1].text
    like_all = soup.select('div[class="TxoC9G6_"]')[2].text
    # ⑥获取ip地址,住居,大学
    douyin_number = soup.select('p[class="wTV10cVL"] span')[0].text.replace('：', ':')
    ip = soup.select('p[class="wTV10cVL"] span')[1].text.replace('：', ':')
    address = soup.select('p[class="wTV10cVL"] span')[2].text
    university = soup.select('p[class="wTV10cVL"] span')[3].text
    # 输出
    print(Fore.LIGHTMAGENTA_EX + str(
        '关注:' + follow_all + '|粉丝: ' + fans_all + '|点赞:' + like_all))

    print(Fore.LIGHTWHITE_EX + '-----------------------------------------------')

    print(Fore.LIGHTBLUE_EX + str(
        douyin_number + '|' + ip + '|' + address + '|' + university))  # 颜色是colorama中的红色,Fore是字体, 教程: https://blog.csdn.net/qq_23845779/article/details/105991806

    print(Fore.LIGHTWHITE_EX + '-----------------------------------------------')

    # ⑦获取置顶视频的点赞数
    # 获取含有"置顶"文本的标签(是个列表!!)
    top_lable_list = soup.find_all(string=re.compile('置顶'))  # ['置顶', '置顶', '置顶']
    # 输出置顶视频的点赞数
    for i in range(0, len(top_lable_list)):
        # 获得含有"置顶"视频字样所在视频的一整块标签
        top_lable_single = top_lable_list[i].parent.parent.parent.parent
        # !成功得到置顶视频点赞数!
        top_like = top_lable_single.select('span')[2].text
        # 输出
        print(Fore.LIGHTCYAN_EX + '置顶视频{}点赞数:{}'.format(i + 1, top_like))
    print(Fore.LIGHTWHITE_EX + '-----------------------------------------------')


    
if __name__ == '__main__':
    headers = {
        'cookie': 'douyin.com; ttwid=1%7CpS_HsCOUf0AUGAwUWbp7ECFOXhWxOBHmKW5M9C6NywQ%7C1682860960%7C4f54c2b1c96fc5ab9ef725f7551bcbd666423679e1095e1bd8183965908877a6; douyin.com; passport_csrf_token=8176efb5e9905cc701088102b93b7711; passport_csrf_token_default=8176efb5e9905cc701088102b93b7711; s_v_web_id=verify_lh3fzdge_JsuOD8BM_WX4c_4sDF_BSbf_P1lPkay0WFdD; ttcid=9698dd3a055541b0ba284b846e0f1bcb90; csrf_session_id=d0247c4e95807e8743533812e3acd5fa; my_rd=1; download_guide=%223%2F20230430%22; passport_assist_user=CkEXlGRvMmeF9d-deZOIWC9I5jEEnNwpnrdkKUyDKA2X4cECO3Py8xCc2zqjTP6GhEwdZo9GBfFwt-7xFZcwwMhJgxpICjzr08O2BpswapVm9aPVhqjb8vSmBbpWuebMPLYRk04LGjA4Ij3DF6bhYZoNd_w4_ZXm3km2si61xGHydF0QyvCvDRiJr9ZUIgED9hQ-Zw%3D%3D; n_mh=oxr5CR3mqWKD4Xc_ISZkSDhK5ElSnspZq265Phb8EwY; sso_uid_tt=4668d4e7d87cc59b5d7b6c8b09a92ad1; sso_uid_tt_ss=4668d4e7d87cc59b5d7b6c8b09a92ad1; toutiao_sso_user=e91169f967e4fe4f3156a516665f9971; toutiao_sso_user_ss=e91169f967e4fe4f3156a516665f9971; sid_ucp_sso_v1=1.0.0-KGUzNGMyZGU0OTFiYTk4YzFkZDg5OTdhZmYyYTAyZTIwZjNiNjExMWUKHwjnh_D7k_TnBBDZ3LmiBhjvMSAMMLnwz_gFOAZA9AcaAmxmIiBlOTExNjlmOTY3ZTRmZTRmMzE1NmE1MTY2NjVmOTk3MQ; ssid_ucp_sso_v1=1.0.0-KGUzNGMyZGU0OTFiYTk4YzFkZDg5OTdhZmYyYTAyZTIwZjNiNjExMWUKHwjnh_D7k_TnBBDZ3LmiBhjvMSAMMLnwz_gFOAZA9AcaAmxmIiBlOTExNjlmOTY3ZTRmZTRmMzE1NmE1MTY2NjVmOTk3MQ; passport_auth_status=6be4b4b7216e41c66b01ae1eb6d673d7%2C; passport_auth_status_ss=6be4b4b7216e41c66b01ae1eb6d673d7%2C; uid_tt=4876c5a54ec9855aaf9023683b0d1799; uid_tt_ss=4876c5a54ec9855aaf9023683b0d1799; sid_tt=ca88280d744888abc7abd19bf34b662f; sessionid=ca88280d744888abc7abd19bf34b662f; sessionid_ss=ca88280d744888abc7abd19bf34b662f; LOGIN_STATUS=1; store-region=cn-gx; store-region-src=uid; bd_ticket_guard_client_data=eyJiZC10aWNrZXQtZ3VhcmQtdmVyc2lvbiI6MiwiYmQtdGlja2V0LWd1YXJkLWl0ZXJhdGlvbi12ZXJzaW9uIjoxLCJiZC10aWNrZXQtZ3VhcmQtY2xpZW50LWNlcnQiOiItLS0tLUJFR0lOIENFUlRJRklDQVRFLS0tLS1cbk1JSUNFekNDQWJxZ0F3SUJBZ0lVUTNiRGxCNC9CZVk4T25qZEYxcTV3MVpDR2ljd0NnWUlLb1pJemowRUF3SXdcbk1URUxNQWtHQTFVRUJoTUNRMDR4SWpBZ0JnTlZCQU1NR1hScFkydGxkRjluZFdGeVpGOWpZVjlsWTJSellWOHlcbk5UWXdIaGNOTWpNd05ETXdNVE16TkRFNVdoY05Nek13TkRNd01qRXpOREU1V2pBbk1Rc3dDUVlEVlFRR0V3SkRcblRqRVlNQllHQTFVRUF3d1BZbVJmZEdsamEyVjBYMmQxWVhKa01Ga3dFd1lIS29aSXpqMENBUVlJS29aSXpqMERcbkFRY0RRZ0FFdXhyVTZiMnNZVUd1eTNFQjF5azY4MVdRRTl3WklSMkhTSHVpcXJ0ajRJZ3dXOUxDaUFYOWNqUWFcbmRJK2tQMC8zYzdEVGgrZzdINHQ4aXU3Q1h0ZlcwNk9CdVRDQnRqQU9CZ05WSFE4QkFmOEVCQU1DQmFBd01RWURcblZSMGxCQ293S0FZSUt3WUJCUVVIQXdFR0NDc0dBUVVGQndNQ0JnZ3JCZ0VGQlFjREF3WUlLd1lCQlFVSEF3UXdcbktRWURWUjBPQkNJRUlPUWgvZDZrbmo5TDIrZGxmNnN6bUdrbUpFMXdtY09BeWd3OTZCcjR5OHRSTUNzR0ExVWRcbkl3UWtNQ0tBSURLbForcU9aRWdTamN4T1RVQjdjeFNiUjIxVGVxVFJnTmQ1bEpkN0lrZURNQmtHQTFVZEVRUVNcbk1CQ0NEbmQzZHk1a2IzVjVhVzR1WTI5dE1Bb0dDQ3FHU000OUJBTUNBMGNBTUVRQ0lBVXZUbWY4bUp2UytiSlFcbjV5Uzgwa1BReitOZG1xcE5NeXhOUitHd3NZM2xBaUI2eVpIcUdGa0MvN3dCUHQ5c1ZDYjg1ZGMvUWxpTS9Ra3Zcbnl4ZTNLRmZHR0E9PVxuLS0tLS1FTkQgQ0VSVElGSUNBVEUtLS0tLVxuIn0=; publish_badge_show_info=%221%2C0%2C0%2C1682862857406%22; xgplayer_user_id=614252535205; strategyABtestKey=%221682970160.535%22; passport_fe_beating_status=true; odin_tt=1583747b1cd9448c0d66ce69c55910fc3b07998684ee584f84466118a809eed880df6a0c666703e7419ae6011c37dac2e312e2a5633dfd4ebeeee26a99d00e59; sid_guard=ca88280d744888abc7abd19bf34b662f%7C1683018264%7C5184000%7CSat%2C+01-Jul-2023+09%3A04%3A24+GMT; sid_ucp_v1=1.0.0-KDFmZGIyZTc2Y2MyOTk4NDJjMjRhMjJhYWIyYjMyZjQzOGM4NmRmZGEKGwjnh_D7k_TnBBCYpMOiBhjvMSAMOAZA9AdIBBoCbGYiIGNhODgyODBkNzQ0ODg4YWJjN2FiZDE5YmYzNGI2NjJm; ssid_ucp_v1=1.0.0-KDFmZGIyZTc2Y2MyOTk4NDJjMjRhMjJhYWIyYjMyZjQzOGM4NmRmZGEKGwjnh_D7k_TnBBCYpMOiBhjvMSAMOAZA9AdIBBoCbGYiIGNhODgyODBkNzQ0ODg4YWJjN2FiZDE5YmYzNGI2NjJm; bd_ticket_guard_server_data=; FOLLOW_NUMBER_YELLOW_POINT_INFO=%22MS4wLjABAAAAqzk7Jv6xYkJBIH9kKtK_YUoy5bH9seZsD7fS80zo4jIj8qBNpVGN1GPGpzheyA1W%2F1683043200000%2F0%2F1683018264553%2F0%22; pwa2=%220%7C1%22; __ac_nonce=064511c5f00061a07ed66; __ac_signature=_02B4Z6wo00f01rYc3nAAAIDAu6aQXZTbZB62PNrAAMniJ4SJ8WRkGKgc2N7mFUS3oVXWNRl3sEw7W9S6HRpA8GaMa..XyW5U0Re9QOiIPQKJmGAO3cvGG8ifCDEbufn-FaT9CS.wXnWO6lMf51; VIDEO_FILTER_MEMO_SELECT=%7B%22expireTime%22%3A1683642089711%2C%22type%22%3A1%7D; FOLLOW_LIVE_POINT_INFO=%22MS4wLjABAAAAqzk7Jv6xYkJBIH9kKtK_YUoy5bH9seZsD7fS80zo4jIj8qBNpVGN1GPGpzheyA1W%2F1683043200000%2F0%2F0%2F1683037991479%22; msToken=P80pf169gIWhBBayMAw6uRmKCLM_foIfF9Oazor4s4bTpPRIIXQJrDd8xyzVZud0CHTSxXToNgoHvWjEuv1adwPxFgGW-UDXY9TjYmVlCj20dCwUtFJZKWRNDSiA0NQ=; home_can_add_dy_2_desktop=%221%22; tt_scid=THOIOZ8QrSJ.sN2ZDeZB9J9JXv1i0619uNoxX1jYmj6xOru27PuOuvJp1LLIOAih91ef; msToken=-8t18h0n56_LZUzfY8gMNYr_7gvNBhyi04FSKKgnPzVwhD1emXX5OhbW_GFnfZsel-BBq8beNTeWxgotxFUeFmWOYQt4GYqmoHGn4zSEuN0l6Av5N8DMa0qW-W9pZl_9',
        'referer': 'https://www.iesdouyin.com/',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36 Edg/112.0.1722.64',
    }
    # eg: url = "https://www.douyin.com/video/7211517706783182118" 或者 https://v.douyin.com/DG1j6FW/ (此url需要重定向获取真实url)
    url = str(input('请输入抖音视频链接: '))
    # url = 'https://v.douyin.com/DXn8k26/'
    
    # 通过重定向获得真实url
    url_real = 'https://www.douyin.com/video/' + str(request.urlopen(url).geturl()).split('video/')[1]
    # 执行方法
    get_info2(get_info1(url=url_real, headers=headers))

# 视频的url(估计是有时间戳,过一段时间地址就失效了)
# "https://v26-web.douyinvod.com/f4359708b1e046ea9276cbc9c1a49c35/6451359b/video/tos/cn/tos-cn-ve-15c001-alinc2/osBNAggC8fAwgAjQIyhzBRNHUEQVgnrDADVZue/"  # print(html)
# 提供的url:https://www.douyin.com/video/7211517706783182118
# 视频页面对应的文件名称为:7211517706783182118
# 单独视频mp4格式的地址对应的名称为-->  ?a=63838&ch=100108&cr=3&dr=0&r=all&........
# 抖音热门创作者页面: https://www.douyin.com/htmlmap/hotauthor_6_1
# 抖音友情链接: https://www.douyin.com/friend_links



