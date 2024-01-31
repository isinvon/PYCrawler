# 爬取博客园信息
import json
import bs4

import requests

url = 'https://www.cnblogs.com/AggSite/AggSitePostList'

data = {
    "CategoryType": "SiteHome",
    "ParentCategoryId": 0,
    "CategoryId": 808,
    "PageIndex": 5,
    "TotalPostCount": 4000,
    "ItemListActionName": "AggSitePostList"
}
headers = {
    "content-type": "application/json; charset=UTF-8",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36",
    # 请填写登录之后的cookie
    "cookie": "",
}


# 使用request请求

res = requests.get(url, json.dumps(data), headers=headers)
res.encoding = res.apparent_encoding
url_stat = res.status_code  # 请求状态
content = res.text  # 内容
soup = bs4.BeautifulSoup(content, 'lxml')
print(soup.prettify())
