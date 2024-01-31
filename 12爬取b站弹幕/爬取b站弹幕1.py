import re
from collections import Counter

import bs4
import pandas
import requests

# 视频url
url = "https://api.bilibili.com/x/v2/dm/web/history/seg.so?type=1&oid=1097737868&date=2023-04-23"
headers = {
    'accept': 'application/json, text/plain, */*',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7',
    # 请填写登陆之后的cookie
    "cookie": "",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36 Edg/112.0.1722.58",
}
response = requests.get(url=url, headers=headers)
response.encoding = response.apparent_encoding
content = response.text
txt = re.findall(':(.*?)@', content, re.S)  # 贪婪匹配
arr = []
for i in range(0, len(txt) - 1):
    # arr = re.findall('[\u4e00-\u9fa5]', txt[i])
    res1 = str(''.join(re.findall('[\u4e00-\u9fa5]', txt[i])))
    # \u4e00-\u9fa5 是匹配中文字符串 : 教程1:https://blog.csdn.net/a786150017/article/details/86004004
    arr.append(res1)

# 词频设置(固定模板)
# 教程范例:https://blog.csdn.net/as604049322/article/details/112486090
with open("停用的词.txt", encoding="utf-8-sig") as f:
    stop_words = f.read().split()
stop_words.extend(['天龙八部', '\n', '\u3000'])  # 添加一些停用的词
stop_words = set(stop_words)

all_words = [word for word in arr if len(word) > 1 and word not in stop_words]
wordcount = Counter(all_words).most_common(5)  # 统计出现最高的5个词,并且显示出现频率
print(wordcount)

f = open(r"弹幕1.txt", 'w', encoding='utf-8')
f.write(str(arr))
f.close()
