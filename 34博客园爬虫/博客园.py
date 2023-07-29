# -*-coding:utf8-*-
import requests
from bs4 import BeautifulSoup
import bs4
import json
import sys
import os
from tomlkit import item

os.chdir(sys.path[0])  # 加上即可使用相对路径(解决相对路径问题)
# os.chdir() 方法用于改变当前工作目录到指定的路径。path-要切换到的新路径。

# 发起GET请求获取网页内容
url = "https://www.cnblogs.com/"
response = requests.get(url)
html_content = response.text

# 使用BeautifulSoup解析HTML内容
soup = BeautifulSoup(html_content, "html.parser")

# 找到所有class为'post-item-title'的<a>标签
post_item_titles = soup.find_all("a", class_="post-item-title")

# 找到所有class为'post-item-summary'的<p>标签
post_item_summarys = soup.find_all("p", class_="post-item-summary")

# 遍历每个<a>标签，提取href和文本内容
result = []
for item_title, item_summary in zip(post_item_titles, post_item_summarys):
    # 获取文章标题
    title = item_title.get_text().strip()
    # 获取文章链接
    href = item_title.get("href").strip()
    # 获取文章摘要
    summary = item_summary.get_text().strip()
    result.append({"title": title, "href": href, "summary": summary})

# 将结果转换为JSON格式
json_data = json.dumps(result, ensure_ascii=False)
with open(file="博客园.json", mode="w", encoding="utf-8") as f:
    # 将json数据写入文件
    f.write(str(json_data))
    f.close()
    
# 打印JSON数据
print(json_data)
