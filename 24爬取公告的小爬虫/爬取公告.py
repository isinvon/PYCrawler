# encoding:utf-8
# !/bin/python3
import re
import requests
import json  # 引入json库
import operator
from lxml import etree

# 教程: 'https://www.52pojie.cn/thread-1666794-1-1.html'
# 爬取的网址
url = '链接地址'
# 请求头
header = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36"}
html = requests.get(url, headers=header).text
etree_html = etree.HTML(html)
names = etree_html.xpath('/html/body/div[1]/div[2]/div[2]/div[2]/div[1]/div/div[1]/p[1]/a/text()')


#                         填入需要爬取的公告xpath
# 读取json
class Read():
    def read_json(self):
        return json.load(open('json文件地址', 'r', encoding="utf-8"))  # /volume1/photo/


read = Read()
a = read.read_json()
b = list(names)
bj = operator.eq(a, b)
c = set(names).difference(set(a))
print(c)
# 比对
# 判断json是否相同
if bj == True:
    print('无变化')
else:
    # 发送post请求
    str = ''.join(str(i) for i in c)
    Cl = str.replace(' ', '\r')
    api = "填入server酱"
    title = u"监测点"
    data1 = {"text": title, "desp": Cl}
    req = requests.post(api, data=data1)
    print('发送成功')
    # 写入json
    filename = 'json文件所在地址'
    insertarr = names  # insertarr为存储数据的数组
    with open(filename, 'w', encoding='utf-8') as file_obj:
        listallarr2 = json.dumps(insertarr, ensure_ascii=False)  # 处理中文乱码问题
        file_obj.write(listallarr2)
exit()
