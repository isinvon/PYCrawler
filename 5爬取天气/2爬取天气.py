# msn天气:
# 雁山区天气的url格式:
# https://www.msn.cn/zh-cn/weather/forecast/in-广西壮族自治区,桂林市,雁山区

import requests
from bs4 import BeautifulSoup
import urllib



def get_weather(html):
    soup = BeautifulSoup(html, 'lxml')
    weather_remind = soup.select("div[id='CurrentWeatherSummary'] p")[0].text
    temperature = soup.select(
        "div[id='OverviewCurrentTemperature'] a")[0]["title"]
    print("现在温度是: " + temperature)
    print(weather_remind)


def get_html(url, headers):
    # 模仿浏览器发送请求
    request = requests.get(url, headers)
    request.encoding = request.apparent_encoding  # 用网页的编码设置编码, 解决中文乱码问题
    return request.text





def main():
    url = "https://www.msn.cn/zh-cn/weather/forecast/in-广西壮族自治区,桂林市,雁山区"
    filename = ""
    headers = {'User-Agent': 'Mozilla/5.0'}  # 表头信息
    html = get_html(url, headers)
    get_weather(html)


if __name__ == '__main__':
    main()
    # get_msn_forecast("河北省")

