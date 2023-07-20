import requests
import re
import time

# 请求头
headers = {
    "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Mobile Safari/537.36"
}


# 定义获取信息的函数
def get_info(url):
    response = requests.get(url=url, headers=headers)
    html = response.content.decode("utf-8")
    print(url, response.status_code)  # 输出url的状态码
    if response.status_code == 200:  # 如果访问正常
        contents = re.findall('<p>(.*?)</p>', html, re.S)
        # 用正则表达式查找所有文字,re.S是re.dotall的缩写,
        #   re.S 的作用是让正则表达式中的点（.）匹配包括换行符在内的所有字符，
        #       以便可以正确地匹配多行文本中的段落。
        for contents in contents:
            new_contents = str(contents).replace('<p>', '').replace('</p>', '')
            f.write(new_contents + '/n')  # 正则获取数据之后写入到txt文件中

        # 插入分割线
        f.write('-------------------------------------------\n'
                '-------------------------------------------\n'
                '-------------------------------------------\n')


if __name__ == '__main__':
    # 构造多页url
    urls = ["http://www.doupoxs.com/doupocangqiong/{}.html".format(str(i)) for i in range(1, 1637)]
    # 新建txt文档,追加的方式
    f = open('doupo.txt', 'a+')

    for url in urls:
        get_info(url)  # 循环调用get_info()函数
        time.sleep(1)
    # 关闭txt文件
    f.close()
