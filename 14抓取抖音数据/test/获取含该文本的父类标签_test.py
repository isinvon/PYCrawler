# 编写爬取Amazon服装行业数据时，遇到一个问题：根据文本内容Next反查包含它的父标签.
# https://blog.csdn.net/RobertChenGuangzhi/article/details/105999610
# testBs.py
from bs4 import BeautifulSoup
import re

'''
    错误示例
    str = """<li class="a-last"><a href="/s?k=red+tshirt&amp;i=fashion-mens&amp;page=2&amp;qid=1588904638&amp;ref=sr_pg_1">Next<span class="a-letter-space"></span><span class="a-letter-space"></span>→</a></li>"""
    soup = BeautifulSoup(str, 'lxml')
    a = soup.find('a', text=re.compile(r"Next"))
    print(a)
'''


str = """<li class="a-last"><a href="/s?k=red+tshirt&amp;i=fashion-mens&amp;page=2&amp;qid=1588904638&amp;ref=sr_pg_1">Next<span class="a-letter-space"></span><span class="a-letter-space"></span>→</a></li>"""

soup = BeautifulSoup(str, 'lxml')
a = soup.find(text=re.compile(r"Next"))

print(a.parent.get('href'))
