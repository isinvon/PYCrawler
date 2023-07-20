from bs4 import BeautifulSoup
import requests
import urllib


class Img():
    url_basic = "https://konachan.net/post/show/353{}"
    headers = {
        'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Mobile Safari/537.36 Edg/110.0.1587.63',
        'cookie': 'cf_clearance=7jkQWxfribBphidBEgoj2lYT11nMvkJvZZXLP8qPve8-1677999453-0-160; country=CN; blacklisted_tags=%5B%22%22%5D; konachan.net=BAh7B0kiD3Nlc3Npb25faWQGOgZFVEkiJThkNDkxM2EwYWRkMDU0MTBlYjlhNjRjMTVmNDkwNzVlBjsAVEkiEF9jc3JmX3Rva2VuBjsARkkiMW9jUm9rZ0M5MWFlMk0veTVqaktJYUNOMlh5Z3AxRVlBdzVDbEhXbkorcXc9BjsARg%3D%3D--951bd140d3a24ebe202274b9b89f828cca69ff75; __utma=20658210.391917013.1677999462.1677999462.1677999462.1; __utmc=20658210; __utmz=20658210.1677999462.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); vote=1; reported_error=1; forum_post_last_read_at=%222023-03-05T08%3A02%3A47%2B01%3A00%22; cf_chl_2=27ec65179f4022c'
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
