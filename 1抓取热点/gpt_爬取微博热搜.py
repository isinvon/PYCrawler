import requests
from bs4 import BeautifulSoup
# 获取网页源码
url = 'https://s.weibo.com/top/summary?cate=realtimehot'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'
}
response = requests.get(url, headers=headers)
html = response.text
# 解析网页源码
soup = BeautifulSoup(html, 'lxml')
hot_list = soup.find_all('tr', class_='td-02')


# 提取数据
for hot in hot_list:
    rank = hot.find('td', class_='td-01 ranktop').title
    title = hot.find('td', class_='td-02').a.title
    link = hot.find('td', class_='td-02').a['href']
    num = hot.find('td', class_='td-02').span.title
    print(rank, title, link, num)
