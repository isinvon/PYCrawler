# coding:utf-8
import keyword

import bs4
import requests
from collections import Counter
import pandas

# 教程1

# url = f'http://comment.bilibili.com/1096871711.xml'  # 其中数字部分是视频的cid号
from wordcloud import WordCloud

url = f'http://comment.bilibili.com/328990210.xml'
# url = 'https://api.bilibili.com/x/player/online/total?aid=782513868&cid=1096871711&bvid=BV1C24y1F7VV&ts=56077484'


headers = {
    # 请填写登陆之后的cookie
    "cookie": "",
    "origin": "https://www.bilibili.com",
    "referer": "https://www.bilibili.com/video/BV1C24y1F7VV/?spm_id_from=333.1007.tianma.1-1-1.click&vd_source=2cdefc492d9cb112d63498710feabcbd",
}
response = requests.get(url=url, headers=headers)
# 调用.encoding属性获取requests模块的编码方式
# 调用.apparent_encoding属性获取网页编码方式
# 将网页编码方式赋值给response.encoding
response.encoding = response.apparent_encoding

html = response.content
soup = bs4.BeautifulSoup(html, 'lxml')
contentList = soup.select("d")

arr = []  # use list to storage the bullet screen

length = len(contentList)
for i in range(0, length):
    arr.append(contentList[i].text)

'''
'gbk' codec can't encode character 解决方法
https://www.cnblogs.com/themost/p/6603409.html
'''

# 词频设置
# 教程范例:https://blog.csdn.net/as604049322/article/details/112486090
with open("停用的词.txt", encoding="utf-8-sig") as f:
    stop_words = f.read().split()
stop_words.extend(['天龙八部', '\n', '\u3000'])  # 添加一些停用的词
stop_words = set(stop_words)

all_words = [word for word in arr if len(word) > 1 and word not in stop_words]
wordcount = Counter(all_words).most_common(20)  # 统计出现最高的20个词,并且显示出现频率
print(wordcount)
# print(all_words)

# 将字符串写入文本中
f = open(r"弹幕2.txt", 'w', encoding='utf-8')
f.write(str(arr))
f.close()

# 读取文本中的信息
with open('弹幕2.txt', 'r', encoding='utf-8') as f:
    string = f.read()

font = r'C:\WINDOWS\FONTS\Arial.TTF'
wc = WordCloud(font_path=font,  # 如果是中文必须要添加这个，否则会显示成框框
               background_color='white',
               width=1000,
               height=800,
               ).generate(string)
print('----------------------------------------------------')
print(string.replace('[', '').replace(']',
      '').replace("'", '').replace(',', ''))
# 词云图中所输入的一定是纯文本,不能是列表或者其他格式, 不然会把其他符号作为词频最高的显示在词云中
wc.to_file('词云图.png')  # 保存图片
print('词云图绘制成功！')
f.close()  # 关闭文件

# content_list = response.text.findAll('<d p=".*?">(.*?)</d>', response.text)
