import bs4
import requests

headers = {
    "content-type": "application/json; charset=UTF-8",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36",
    # 请填写登录之后的cookie
    "cookie": "",
}

def get_info(url, page_end):
    for i in range(1, page_end+1):  # 循环页数
        url = url.format(i + 1)  # 补全url
        print(url)
        response = requests.get(url=url, headers=headers)
        content = response.text
        html = content
        soup = bs4.BeautifulSoup(html, 'lxml')
        for num in range(1, 20):
            article = soup.select("article[class='post-item']")[num]
            text = soup.select("div[class='post-item-text']")[num]
            title = text.select("a[class='post-item-title']")[0].text
            link = text.select("a[class='post-item-title']")[0].get("href")
            footer = article.select("footer[class='post-item-foot']")  # 每一章的脚
            author = footer[0].select("a span")[0].text  # 作者
            like = footer[0].select("a span")[1].text  # 喜欢
            comment = footer[0].select("a span")[2].text  # 评论
            look = footer[0].select("a span")[3].text  # 观看

            print("😊" + title + "\n"
                  + "   点赞:" + like + " 评论:" + comment + "观看:" + look + " 作者:" + author + "\n"
                  + "   => " + link + "\n"
                  + "--------------------------")


if __name__ == '__main__':
    url = "https://www.cnblogs.com/#p5"  # 后面是数字
    page_end = 2
    print(type(page_end))
    get_info(url, page_end)