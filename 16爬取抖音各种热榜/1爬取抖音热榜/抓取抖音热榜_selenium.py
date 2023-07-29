# -*-coding:utf8-*-
import os, sys
import re
import json
import time
from webbrowser import Chrome
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
from pathlib import Path

os.chdir(sys.path[0])  # 加上即可使用相对路径(解决相对路径问题)
# os.chdir() 方法用于改变当前工作目录到指定的路径。path-要切换到的新路径。


# import sys
# reload(sys)
# sys.setdefaultencoding('utf8')


# https://zhuanlan.zhihu.com/p/412261792zx

# 爬取创作者平台:https://creator.douyin.com/billboard/home
#     教程: https://blog.csdn.net/weixin_43582101/article/details/107082121
# 注意点:
#   requests得不到ajax动态加载的内容，只能得到查看源代码时得到的内容，需要找数据接口来请求
#     可以用selenium来模仿用户操作
# selenium最新版的新特性:https://zhuanlan.zhihu.com/p/475212818


headers = {
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7',
    'cookie': 'douyin.com; passport_csrf_token=8176efb5e9905cc701088102b93b7711; passport_csrf_token_default=8176efb5e9905cc701088102b93b7711; s_v_web_id=verify_lh3fzdge_JsuOD8BM_WX4c_4sDF_BSbf_P1lPkay0WFdD; ttcid=9698dd3a055541b0ba284b846e0f1bcb90; csrf_session_id=d0247c4e95807e8743533812e3acd5fa; my_rd=1; download_guide=%223%2F20230430%22; passport_assist_user=CkEXlGRvMmeF9d-deZOIWC9I5jEEnNwpnrdkKUyDKA2X4cECO3Py8xCc2zqjTP6GhEwdZo9GBfFwt-7xFZcwwMhJgxpICjzr08O2BpswapVm9aPVhqjb8vSmBbpWuebMPLYRk04LGjA4Ij3DF6bhYZoNd_w4_ZXm3km2si61xGHydF0QyvCvDRiJr9ZUIgED9hQ-Zw%3D%3D; n_mh=oxr5CR3mqWKD4Xc_ISZkSDhK5ElSnspZq265Phb8EwY; sso_uid_tt=4668d4e7d87cc59b5d7b6c8b09a92ad1; sso_uid_tt_ss=4668d4e7d87cc59b5d7b6c8b09a92ad1; toutiao_sso_user=e91169f967e4fe4f3156a516665f9971; toutiao_sso_user_ss=e91169f967e4fe4f3156a516665f9971; sid_ucp_sso_v1=1.0.0-KGUzNGMyZGU0OTFiYTk4YzFkZDg5OTdhZmYyYTAyZTIwZjNiNjExMWUKHwjnh_D7k_TnBBDZ3LmiBhjvMSAMMLnwz_gFOAZA9AcaAmxmIiBlOTExNjlmOTY3ZTRmZTRmMzE1NmE1MTY2NjVmOTk3MQ; ssid_ucp_sso_v1=1.0.0-KGUzNGMyZGU0OTFiYTk4YzFkZDg5OTdhZmYyYTAyZTIwZjNiNjExMWUKHwjnh_D7k_TnBBDZ3LmiBhjvMSAMMLnwz_gFOAZA9AcaAmxmIiBlOTExNjlmOTY3ZTRmZTRmMzE1NmE1MTY2NjVmOTk3MQ; passport_auth_status=6be4b4b7216e41c66b01ae1eb6d673d7%2C; passport_auth_status_ss=6be4b4b7216e41c66b01ae1eb6d673d7%2C; uid_tt=4876c5a54ec9855aaf9023683b0d1799; uid_tt_ss=4876c5a54ec9855aaf9023683b0d1799; sid_tt=ca88280d744888abc7abd19bf34b662f; sessionid=ca88280d744888abc7abd19bf34b662f; sessionid_ss=ca88280d744888abc7abd19bf34b662f; LOGIN_STATUS=1; store-region=cn-gx; store-region-src=uid; bd_ticket_guard_client_data=eyJiZC10aWNrZXQtZ3VhcmQtdmVyc2lvbiI6MiwiYmQtdGlja2V0LWd1YXJkLWl0ZXJhdGlvbi12ZXJzaW9uIjoxLCJiZC10aWNrZXQtZ3VhcmQtY2xpZW50LWNlcnQiOiItLS0tLUJFR0lOIENFUlRJRklDQVRFLS0tLS1cbk1JSUNFekNDQWJxZ0F3SUJBZ0lVUTNiRGxCNC9CZVk4T25qZEYxcTV3MVpDR2ljd0NnWUlLb1pJemowRUF3SXdcbk1URUxNQWtHQTFVRUJoTUNRMDR4SWpBZ0JnTlZCQU1NR1hScFkydGxkRjluZFdGeVpGOWpZVjlsWTJSellWOHlcbk5UWXdIaGNOTWpNd05ETXdNVE16TkRFNVdoY05Nek13TkRNd01qRXpOREU1V2pBbk1Rc3dDUVlEVlFRR0V3SkRcblRqRVlNQllHQTFVRUF3d1BZbVJmZEdsamEyVjBYMmQxWVhKa01Ga3dFd1lIS29aSXpqMENBUVlJS29aSXpqMERcbkFRY0RRZ0FFdXhyVTZiMnNZVUd1eTNFQjF5azY4MVdRRTl3WklSMkhTSHVpcXJ0ajRJZ3dXOUxDaUFYOWNqUWFcbmRJK2tQMC8zYzdEVGgrZzdINHQ4aXU3Q1h0ZlcwNk9CdVRDQnRqQU9CZ05WSFE4QkFmOEVCQU1DQmFBd01RWURcblZSMGxCQ293S0FZSUt3WUJCUVVIQXdFR0NDc0dBUVVGQndNQ0JnZ3JCZ0VGQlFjREF3WUlLd1lCQlFVSEF3UXdcbktRWURWUjBPQkNJRUlPUWgvZDZrbmo5TDIrZGxmNnN6bUdrbUpFMXdtY09BeWd3OTZCcjR5OHRSTUNzR0ExVWRcbkl3UWtNQ0tBSURLbForcU9aRWdTamN4T1RVQjdjeFNiUjIxVGVxVFJnTmQ1bEpkN0lrZURNQmtHQTFVZEVRUVNcbk1CQ0NEbmQzZHk1a2IzVjVhVzR1WTI5dE1Bb0dDQ3FHU000OUJBTUNBMGNBTUVRQ0lBVXZUbWY4bUp2UytiSlFcbjV5Uzgwa1BReitOZG1xcE5NeXhOUitHd3NZM2xBaUI2eVpIcUdGa0MvN3dCUHQ5c1ZDYjg1ZGMvUWxpTS9Ra3Zcbnl4ZTNLRmZHR0E9PVxuLS0tLS1FTkQgQ0VSVElGSUNBVEUtLS0tLVxuIn0=; publish_badge_show_info=%221%2C0%2C0%2C1682862857406%22; xgplayer_user_id=614252535205; passport_fe_beating_status=true; sid_guard=ca88280d744888abc7abd19bf34b662f%7C1683018264%7C5184000%7CSat%2C+01-Jul-2023+09%3A04%3A24+GMT; sid_ucp_v1=1.0.0-KDFmZGIyZTc2Y2MyOTk4NDJjMjRhMjJhYWIyYjMyZjQzOGM4NmRmZGEKGwjnh_D7k_TnBBCYpMOiBhjvMSAMOAZA9AdIBBoCbGYiIGNhODgyODBkNzQ0ODg4YWJjN2FiZDE5YmYzNGI2NjJm; ssid_ucp_v1=1.0.0-KDFmZGIyZTc2Y2MyOTk4NDJjMjRhMjJhYWIyYjMyZjQzOGM4NmRmZGEKGwjnh_D7k_TnBBCYpMOiBhjvMSAMOAZA9AdIBBoCbGYiIGNhODgyODBkNzQ0ODg4YWJjN2FiZDE5YmYzNGI2NjJm; bd_ticket_guard_server_data=; pwa2=%220%7C1%22; d_ticket=667992a7e93f68b4ca96e8d18917188d5d745; __live_version__=%221.1.0.9069%22; live_can_add_dy_2_desktop=%220%22; strategyABtestKey=%221683129864.558%22; SEARCH_RESULT_LIST_TYPE=%22single%22; MONITOR_WEB_ID=6af2f4a0-2986-4d46-83c1-614a7819d53d; _tea_utm_cache_1243=undefined; VIDEO_FILTER_MEMO_SELECT=%7B%22expireTime%22%3A1683738364638%2C%22type%22%3A1%7D; FOLLOW_NUMBER_YELLOW_POINT_INFO=%22MS4wLjABAAAAqzk7Jv6xYkJBIH9kKtK_YUoy5bH9seZsD7fS80zo4jIj8qBNpVGN1GPGpzheyA1W%2F1683216000000%2F0%2F0%2F1683180527150%22; __ac_signature=_02B4Z6wo00f01jeUKegAAIDAOi5nxFIHml43pC1AAOnEDVqNBvvDmKdUweOHKqfvL-P3YlSyCdt-sOHz1Kdc0qDViqx86HDL6MV8uKETWo1pHzWooYQYiUIxRis0-4yPBvdQnKNwXvL.YsJub3; ttwid=1%7CpS_HsCOUf0AUGAwUWbp7ECFOXhWxOBHmKW5M9C6NywQ%7C1683179538%7C22f9025d7602bbdd215e99090f76081be069f7a8bc96d1175861da5bf0bd97b1; odin_tt=893c5f542b6b2f6e554d47fd1f72c66f3a49a4c1dd1c930081af4948b581a0115cc42e308addb2648b925a34abeb9a2e; __ac_nonce=06453911c00899eb97176; FOLLOW_LIVE_POINT_INFO=%22MS4wLjABAAAAqzk7Jv6xYkJBIH9kKtK_YUoy5bH9seZsD7fS80zo4jIj8qBNpVGN1GPGpzheyA1W%2F1683216000000%2F0%2F1683198397376%2F0%22; tt_scid=ccGyZx9w5rZi2sFssQx2wXyOq8Wz-Z-T.KCKkyurfeJihItOt0bRcnyur5mKtYvz0c5e; msToken=IB2T4XAnKU85b8ST6r-w8FzFo5GVQWzFCl0ZX4yqwL1Ue0R9K1mr1hW8JwWRIQ4qrk41eVHl9i8kjxjiuc2Ap7zwGkN3_m5dEOaxmaH19nUrBGi5L2VsoafRac_7i2E=; msToken=t1yujoW61u01PsVJXPep4aUfkXXU3J2b3tb-1Pe9XVVvCnzxkqNJcYOaMY0K_eqt3d8qb5EFkyeDsX4p_zoXXvyehlD8uvA704NyjC2FYBTEFvqvsZGkeoPA7l_Ko8w=; home_can_add_dy_2_desktop=%220%22',
    'referer': 'https://www.douyin.com/hot',
    'sec-ch-ua': '"Chromium";v="112", "Microsoft Edge";v="112", "Not:A-Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36 Edg/112.0.1722.68'
}
url = 'https://www.douyin.com/hot'

user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36 Edg/112.0.1722.68'


# 热榜是动态的,使用request是获取不到的
def get_hot():
    global len
    hot_list = []
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        # 设置selenium无界面(无头模式)
        options = webdriver.ChromeOptions()
        options.use_chromium = True  # 是否开启浏览器可视化
        options.add_argument('headless')  # selenium设置无头模式可以让浏览器在爬取的时候不启动窗口(写headless和--headless都可以)
        options.add_argument(f'user-agent={user_agent}')  # 如果无头模式得到的信息少, 那就加上用户代理, f即format()
        options.page_load_strategy = 'normal'  # 设置selenium的加载模式https://zhuanlan.zhihu.com/p/453590557
        '''add_argument常用参数表: https://blog.csdn.net/qq_42059060/article/details/104522492'''

        driver = webdriver.Chrome(
            executable_path='chromedriver.exe', options=options)  # 获得chrome浏览器的驱动  # executable_path是驱动的名字(使用的前提是配置了环境变量)
        driver.get('https://www.douyin.com/hot')
        # driver.implicitly_wait(7) # 等待10s
        html = driver.page_source  # 得到真实的html
        # print(html)
        # 得到html之后直接取值是得不到的,得将html下载到本地,对文本进行爬取
        with open(file='抖音热榜源码.txt', mode='w+', encoding='utf-8') as f:  # w新建只写，w+新建读写
            f.write(html)
            f.close()
        # 打开已经写入本地的源码文件
        f = open('抖音热榜源码.txt', encoding='utf-8')  # 打开文件
        content = f.read()  # 读取文件
        soup = bs4.BeautifulSoup(content, 'lxml')
        # ①获取新闻标题,链接,热度(注意有个置顶的新闻) # 保存到三维数组eg:data.append([aeg1,agr2,arg3])
        len = len(soup.select('ul[class="IeYdlA10"] li'))  # 51
        for i in range(0, len):

            hot_title = soup.select('ul[class="IeYdlA10"] h3')[i].text.strip()  # strip()去除头尾空格
            hot_link = 'https://www.douyin.com' + soup.select('ul[class="IeYdlA10"] a')[i].get('href')
            # 判断是否是置顶的新闻(置顶新闻无热度)
            if i == 0:
                hot_heat = '置顶'
                hot_list.append(
                    [Fore.WHITE + '[{}]'.format(i + 1), Fore.GREEN + str(hot_title), Fore.RED + str(hot_heat), Fore.BLUE + str(hot_link)])
            else:
                hot_heat = soup.select('ul[class="IeYdlA10"] li span[class="JfqK03EE"]')[i - 1].text
                hot_list.append(
                    [Fore.WHITE + '[{}]'.format(i + 1), Fore.GREEN + str(hot_title), Fore.RED + str(hot_heat), Fore.BLUE + str(hot_link)])
        # 教程: https://blog.csdn.net/qq_42415326/article/details/104767355
        table = PrettyTable(['序号', '标题', '热度', '链接'])
        table.add_rows(hot_list)
        print(table)
        # 关闭文件读取
        f.close()
        time.sleep(5)
        # 关闭浏览器对象
        driver.close()


# 其中含有热榜的信息json形式-> "https://www.douyin.com/aweme/v1/web/hot/search/list/?device_platform=webapp&aid=6383&channel=channel_pc_web&detail_list=1&source=6&pc_client_type=1&version_code=170400&version_name=17.4.0&cookie_enabled=true&screen_width=1204&screen_height=803&browser_language=zh-CN&browser_platform=Win32&browser_name=Edge&browser_version=112.0.1722.68&browser_online=true&engine_name=Blink&engine_version=112.0.0.0&os_name=Windows&os_version=10&cpu_core_num=8&device_memory=8&platform=PC&downlink=10&effective_type=4g&round_trip_time=50&webid=7227832700508931617&msToken=zpMg_FZmIPGFJtPwQVtPqxTTmvVAIwED9htDC5oOSGynU2MF0O1TKzDfg9pYCmTe7SJd4ZMyauPBxl43rYBrzwmdAFdDwZ065RTAO8Xvbthg_ASGWCjQxZdyo_uPYSF2&X-Bogus=DFSzswVOaKxANSaNtCA/ZxanArWE"

if __name__ == '__main__':
    # 如果还是无法访问就多加几个请求头
    get_hot()
