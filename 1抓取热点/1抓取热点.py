import urllib
import bs4
from bs4 import BeautifulSoup
import requests


def get_hot(html):
    soup = BeautifulSoup(html, 'lxml')
    # hot = soup.select("ls
    # div[class='vue-recycle-scroller__item-view'] ")
    # hot = soup.select("div[class='vue-recycle-scroller__item-wrapper'] ")
    # print(hot)


def get_html(url, headers):
    response = requests.get(url, headers)
    response.encoding = response.apparent_encoding
    return response.text


def main():
    url = "https://weibo.com/hot/search"
    headers = {
        'User-Agent': 'Mozilla/5.0',
        # 'cookie': 'SINAGLOBAL=1127422090395.0383.1677333402874; login_sid_t=6fd501faa198b431d141da46e36abf91; cross_origin_proto=SSL; _s_tentry=cn.bing.com; UOR=,,cn.bing.com; wb_view_log=1584*10561.5674999952316284; XSRF-TOKEN=_xQbXMxHxzttthAgyYyPXY6K; Apache=2282365249758.7866.1677951822828; ULV=1677951822831:2:1:1:2282365249758.7866.1677951822828:1677333402877; SUB=_2A25JB_XcDeRhGeFG6VYY9yjFyDuIHXVqdWAUrDV8PUNbmtAGLWXNkW9NeejhdTA-kq2jxQO3ZfZfdgKR_dWpiuZv; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WFp8XIeQiba_CObGbL6c4Vk5JpX5KzhUgL.FoMReoB4S0q4e0M2dJLoIp7LxKML1KBLBKnLxKqL1hnLBoMN1hzX1KMc1KeN; ALF=1709488395; SSOLoginState=1677952396; PC_TOKEN=056100be9b; WBPSESS=ymfvqD0sw3HEdn-XndbaYaE00KF5CwKc77ZlRileOyU_6nRMf0gyCQ89w14M7-6hsiZ8ztOa6Qilw1VgPpI5_P2jjJyw6af8cDM2o3UTktuPJE0c5kbp85xXnIWWmADGY2o3-Zdn-wBHJGax3D4etA=='
    }
    # headers = {
    #     'User-Agent': "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Mobile Safari/537.36"
    # }
    html = get_html(url, headers)
    get_hot(html)

    print(html)


if __name__ == '__main__':
    main()
