import requests
from bs4 import BeautifulSoup
import json

url = "https://www.cnblogs.com/"

# 发送GET请求获取网页内容
response = requests.get(url)
html_content = response.content

# 使用BeautifulSoup解析网页内容
soup = BeautifulSoup(html_content, "html.parser")

# 查找所有符合条件的div标签
div_tags = soup.find_all("div", class_="card")

# 定义一个列表保存解析结果
result = []

# 遍历每个div标签
for div in div_tags:
    # 查找当前div标签下的ul标签
    ul_tag = div.find("ul", class_="card-title")
    print(ul_tag)

    if ul_tag is not None:
        # 查找ul标签下的所有span标签和a标签
        span_tags = ul_tag.find_all("span")
        a_tags = ul_tag.find_all("a")

        # 获取span标签和a标签中的内容和href值
        spans = [span.get_text() for span in span_tags]
        links = [{"text": a.get_text(), "href": a.get("href")} for a in a_tags]

        # 将结果添加到列表中
        result.append({"spans": spans, "links": links})

# 将结果转换为JSON格式
json_result = json.dumps(result, ensure_ascii=False)

# 打印结果
print(json_result)
