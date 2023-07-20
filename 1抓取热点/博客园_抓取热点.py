from pandas.core.frame import DataFrame
import requests
from bs4 import BeautifulSoup
import bs4
# 定义获取页面信息函数


def get_html(url, headers):
    r = requests.get(url, headers=headers)
    r.encoding = r.apparent_encoding  # 解决中文字符编码问题
    return r.text


# 建立空表格 准备数据填充
name = []
rank = []
times = []
# 定义解析页面函数


def get_pages(html):
    soup = BeautifulSoup(html, 'html.parser')  # 使用BeautifulSoup库解析页面
    all_topics = soup.find_all('tr')[1:]  # 获取标签内容
    for each_topic in all_topics:

        topic_times = each_topic.find('td', class_='last')  # 热度
        topic_rank = each_topic.find('td', class_='first')  # 排名
        topic_name = each_topic.find('td', class_='keyword')  # 标题目
        if topic_rank != None and topic_name != None and topic_times != None:
            topic_rank = each_topic.find('td', class_='first').get_text().replace(
                ' ', '').replace('\n', '')
            rank.append(topic_rank)  # 填充数据
            topic_name = each_topic.find('td', class_='keyword').get_text().replace(
                ' ', '').replace('\n', '')
            name.append(topic_name)
            topic_times = each_topic.find(
                'td', class_='last').get_text().replace(' ', '').replace('\n', '')
            times.append(topic_times)

            tplt = "排名：{0:^4}\t标题：{1:{3}^15}\t热度：{2:^8}"

# 定义主函数


def main():
    url = 'http://top.baidu.com/buzz?b=1&fr=20811'
    headers = {'User-Agent': 'Mozilla/5.0'}  # 表头信息
    html = get_html(url, headers)
    get_pages(html)


if __name__ == '__main__':
    main()
print(times)
print(name)
print(rank)
# 使用pandans保存数据
D = {"排名": rank,
     "标题": name,
     "热度": times}
data = DataFrame(D)
print(data)
# 生成CSV文件
filename = "redian.csv"
data.to_csv(filename, index=False)
