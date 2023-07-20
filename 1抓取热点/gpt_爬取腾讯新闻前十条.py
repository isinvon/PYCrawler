import requests
from bs4 import BeautifulSoup
# 获取网页源码
url = 'https://news.qq.com/'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'
}
response = requests.get(url, headers=headers)
html = response.text
# 解析网页源码
soup = BeautifulSoup(html, 'lxml')
news_list = soup.find_all('div', class_='list')
# 提取数据
for news in news_list[:10]: 
    title = news.a.title
    link = news.a['href']
    print(title, link)
    