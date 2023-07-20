import requests
from lxml import etree
import os


headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Safari/537.36',
}


def download(img, count):
    r = requests.get(img, headers=headers)
    pic = r.content
    try:
        with open('{}.jpg'.format(count), 'wb') as f:
            f.write(pic)
            print('{}.jpg-----下载成功'.format(count))
    except:
        print('下载失败！')


def get_img(img_url):
    r = requests.get(img_url, headers=headers)
    html = r.content.decode('gbk')
    tree = etree.HTML(html)
    # 图片链接
    img_list = tree.xpath(
        '//div[@id="main"]/div[@class="slist"]/ul/li/a/img/@src')
    # print(img_list, len(img_list))
    count = 1
    for img in img_list:
        img = 'http://pic.netbian.com' + img
        # 下载图片
        download(img, count)
        count = count + 1


def main():
    # 启始url
    url = 'http://pic.netbian.com/4kdongman/'
    req = requests.get(url, headers=headers)
    html = req.content.decode('gbk')
    # print(html)
    tree = etree.HTML(html)
    # 提取壁纸页数
    num = tree.xpath('//div[@class="page"]/a[last() - 1]/text()')[0]
    for i in range(int(num)):
        # 创建目录用于下载
        path = 'F:\\图片文件\\高清壁纸\\第{}页\\'.format(i + 1)
        if not os.path.exists(path):
            os.makedirs(path)
        # 改变当前工作目录
        os.chdir(path)
        print('----------第{}页---------正在下载-----'.format(i + 1))

        img_url = url + 'index_{}.html'.format(i + 1)
        if i == 0:
            img_url = url
        # print(img_url)
        # 获取图片链接
        get_img(img_url)


if __name__ == '__main__':
    main()
