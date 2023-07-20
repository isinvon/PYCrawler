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
    "cookie": "__gads=ID=85ea91454ff7ae2a:T=1661687799:S=ALNI_MZ65JoXR05zq1W3T-VaRRv2ZNt33A; _clck=t1351q|1|f8y|0; _ga_3Q0DVSGN10=GS1.1.1676447541.2.1.1676447564.37.0.0; _ga=GA1.2.486211484.1655131579; Hm_lvt_32247700466dcd5fcde2763a97d5c0e3=1677086777; .AspNetCore.Antiforgery.b8-pDmTq1XM=CfDJ8M-opqJn5c1MsCC_BxLIULkEBrkZ-GWjgWHK5gU5qbIsF9CDZy_nOH99Yu6wo8tEhqf9tv0LNVm8fYeICfVCCGiWo1CKZjR7MB9CpLob-dH7B2CTPDt_ooNNCQh5SvN9kMM9RtxDVPxMEArFsY7kRW4; cto_bundle=T37qz19aJTJCdEJkWHolMkZ6cEZXQXNPbnNKaE5Vdmp6U080OVZCeG9HZGJ5a01kT3dCZk5xTTMlMkJvQlhqNUhWU1VlT1cxJTJCQ3cxeDZJV2t0WWdwS2twWkVEbWpDN0c0UUZGcWR5UVR1UFRGODElMkZPUkhObkFlZlNZazZ5c1BHTUolMkJOcTFkb1JlMm1pc0xFeG5OaU9uZjhIQyUyQnElMkI5U0RnJTNEJTNE; Hm_lvt_866c9be12d4a814454792b1fd0fed295=1680092546; _gid=GA1.2.1407189783.1681206623; _gat_gtag_UA_476124_1=1; __gpi=UID=0000092d001786a0:T=1661687799:RT=1681206624:S=ALNI_MZPIJqiVbfHw8A7v5uOjGsLCfq4fA; Hm_lpvt_866c9be12d4a814454792b1fd0fed295=1681206665",
}


# 使用request请求

res = requests.get(url, json.dumps(data), headers=headers)
res.encoding = res.apparent_encoding
url_stat = res.status_code  # 请求状态
content = res.text  # 内容
soup = bs4.BeautifulSoup(content, 'lxml')
print(soup.prettify())
