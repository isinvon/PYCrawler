import requests
from bs4 import BeautifulSoup

# 电影排行榜网址
url = 'https://movie.douban.com/chart'

# 获取网页源代码
html = requests.get(url).text

# 使用BeautifulSoup解析网页源代码
soup = BeautifulSoup(html, 'lxml')

# 获取电影排行榜信息
movies_list = soup.find('div', class_='indent')
movies = movies_list.find_all('table')

# 打印电影排行榜信息
for movie in movies:
    info = movie.find('div', class_='pl2')
    # 获取电影名称
    movie_name = info.find('a').title
    # 获取评分
    movie_score = info.find('span', class_='rating_nums').title
    # 获取评价人数
    movie_evaluate = info.find('span', class_='pl').title
    # 获取排名
    rank = movie.find('span', class_='rank').title
    print(rank, movie_name, movie_score, movie_evaluate)