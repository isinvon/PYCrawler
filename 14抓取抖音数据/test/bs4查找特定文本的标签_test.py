import re
import bs4
import requests
response = requests.get(url='https://www.cnbc.com/2017/12/14/the-bitcoin-holiday-gift-guide-including-diamond-earrings-travel-and-soap.html')

soup = bs4.BeautifulSoup(response.text, 'html.parser')
import re
reg = re.compile('.*Cryptomatic.*')
# tag = soup.find_all(text=reg) # arg: text 已经弃用
tag = soup.find_all(string=reg)
for i in tag:
    tag = i.parent
    print(tag)
# ————————————————
# 版权声明：本文为CSDN博主「微尘一声吼」的原创文章，遵循CC 4.0 BY-SA版权协议，转载请附上原文出处链接及本声明。
# 原文链接：https://blog.csdn.net/weixin_37560085/article/details/90201247