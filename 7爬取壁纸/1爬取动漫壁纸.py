from bs4 import BeautifulSoup
import requests
import urllib


class Img():
    # 此网站需要梯子
    url_basic = "https://konachan.net/post/show/353{}"
    headers = {
        'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Mobile Safari/537.36 Edg/110.0.1587.63',
        # 请填写登录之后的cookie
        'cookie': ''
    }

    # 下载图片

    def get_img(self):
        # for num in range(550, 600+1):
        for num in range(555, 557):
            url = self.url_basic.format(num)
            request = requests.get(url=url, headers=self.headers)
            request.encoding = request.apparent_encoding  # 设置编码格式, 防止中文乱码
            html = request.text
            soup = BeautifulSoup(html, "lxml")
            link = soup.select("div[id='right-col']")
            name = soup.select("div[class='content']")
            print(link)


if __name__ == '__main__':
    img = Img()  # 创建类对象
    img.get_img()
