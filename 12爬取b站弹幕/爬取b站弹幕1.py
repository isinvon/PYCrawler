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
    "cookie": "buvid3=0AAC01A8-3B72-9EC0-5FE5-8EF31FC5B8EF04084infoc; b_nut=1677643404; CURRENT_FNVAL=4048; _uuid=47DCA8AA-4DC5-8616-B5AD-B81A62F2F59301715infoc; buvid4=997B36F3-736D-07F2-ECE8-9ABE682DE17484923-022032422-x4m6iybJgymEoDfZzX0SsA%3D%3D; rpdid=|(u)mYY)JkY|0J'uY~~YRJR|Y; i-wanna-go-back=-1; header_theme_version=CLOSE; nostalgia_conf=-1; buvid_fp_plain=undefined; LIVE_BUVID=AUTO3016778995947989; i-wanna-go-feeds=2; CURRENT_QUALITY=64; CURRENT_PID=54e74a00-cec0-11ed-85e8-a99369173808; DedeUserID=446423825; DedeUserID__ckMd5=44b4dac40b10cd65; b_ut=5; FEED_LIVE_VERSION=V8; SESSDATA=f05f091d%2C1696864838%2C55f14%2A41; bili_jct=f4b42dfae88858e692ae8331777aab4f; sid=65e0t1ji; PVID=2; home_feed_column=5; browser_resolution=1403-824; innersign=1; b_lsid=2AAB7E78_187AEE2C774; fingerprint=8dbf2645293d180dbaaf2603b7579159; buvid_fp=755c74b02ff3a96fb9b68ab66148c68c; bp_video_offset_446423825=787821947188674600",
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
