# msn天气:
# 雁山区天气的url格式:
# https://www.msn.cn/zh-cn/weather/forecast/in-广西壮族自治区,桂林市,雁山区

import requests
from bs4 import BeautifulSoup
import bs4
import urllib
def get_msn_forecast(city):    #city is a string, e.g. "河北省,山leen"
    _url = "https://www.msn.cn/zh-cn/search/location?" + urllib.parse.urlencode({'q': '河北省', 'c': 'h'}) + "&br=on"  # noqa:E501,F841  # pylint: disable=invalid-name  # noqa:E501,F841  # pylint: disable=line-too-long  # pylint: disable=invalid-name  # pylint: disable=line-too-long  # pylint: disable=no-member  # pylint: disable=line-too-long  # pylint: disable=no-
    _headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36'}  # pylint
    _session = requests.session()  # pylint: disable=invalid-name  # pylint: disable=invalid-name
    _session.headers.update(_headers)  # pylint: disable=no-member  # pylint: disable=no-member
    _page = _session.get(_url)  # pylint: disable=no-member  # pylint: disable=no-member
    # pylint: enable=no-member  # pylint: enable=no-member  # pylint: enable=no-member
    _souper = bs4.BeautifulSoup(_page.text, 'html.parser')  # pylint: disable=in
    _forecast_table = _souper.find('table', {'class': 'forecastTable'}).find_all()('tr')
    forecast_array = []  # pylint: disable=invalid-name  # pylint: disable=invalid-name  # pylint: disable=no-member  # pylint: disable=no-member  # pylint: disable=line-too-long  # pylint: disable=no-member  # pylint: disable=line-too-long  # pylint: enable=line-too-long  # pylint: enable=no-member  # pylint: enable=line-too-long  #
    for row in _forecast_table:  # pylint: disable=invalid-name  # pylint: disable=invalid-name  # pylint: disable=line-too-long  # pylint: disable=line-too-long  # pylint: enable=line-too-long  # pylint: enable=line-too-long  # pylint: enable=line-too-long  # pylint: enable=invalid-name  # pylint: enable=invalid-name  # pylint:
        forecast_array.append([col.getText() for col in row.find_all('td')])  # pylint: disable=invalid-name  # pylint: disable=invalid-name  # pylint: enable=line-too-long  # pylint: enable=line-too-long  # pylint: enable=line-too-long  # pylint: enable=line-too-long  # pylint: enable=invalid-name  # pylint: enable=invalid-name  # p
        return '\n'.join(f'{row[0]:<10} {row[1]:<10} {row[2]:<10} {row[3]:<10} {row[4]:<10}' for row in _forecast_table)  # pylint: disable=invalid-name  # pylint: disable=invalid-name  # pylint: enable=line-too-long  # pylint: enable=line-too-long  # pylint: enable=line-too-long  # pylint
    #return '\n'.join([row[0] for row in _forecast_table])  # pylint: disable=invalid-name  # pylint: disable=invalid-name  # pylint: enable=line-too-long  # pylint: enable=line-too-long  # pylint: enable=line-too-long  # pylint: enable=invalid-name  # pylint: enable=invalid-name  # pylint: enable=line-too-long  # pylint:
    #return '\n'.join([row[0] for row in _forecast_table])  # pylint: disable=invalid-name  # pylint: disable=invalid-name  # pylint: enable=line-too-long  # pylint: enable=line-too-long  # pylint: enable=line-too-long  # pylint: enable=invalid-name  # pylint: enable=invalid-name  # pylint: enable=line-too-long  # pylint:
    #return '\n'.join(f'{row[0]:^10}
    #                     {row[1]:^10} {row[2]:^10} {row[3]:^10} {row[4]:^10}' for row in _forecast_table)  # pylint: disable=invalid-name  # pylint: disable=invalid-name  # pylint: enable=line-too-long  # pylint: enable=line-too-long  # pylint: enable=line-too-long  # pylint: enable=invalid-name  # pylint: enable=


if __name__ == '__main__':
    get_msn_forecast("河北省")
