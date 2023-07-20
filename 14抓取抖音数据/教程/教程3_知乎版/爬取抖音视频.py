import requests
import json


class Douyin:
    def page_num(self, max_cursor):
        # 网址后面的随机参数（我实在分析不出规律）
        random_field = 'RVb7WBAZG.rGG9zDDDoezEVW-0&dytk=a61cb3ce173fbfa0465051b2a6a9027e'
        # 网址的主体
        url = 'https://www.iesdouyin.com/web/api/v2/aweme/post/?sec_uid' \
              '=MS4wLjABAAAAF5ZfVgdRbJ3OPGJPMFHnDp2sdJaemZo3Aw6piEtkdOA&count=21&max_cursor=0&aid=1128&_signature=' +\
              random_field
        # 请求头
        headers = {
            'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/81.0.4044.129 Safari/537.36',
        }
        response = requests.get(url, headers=headers).text
        # 转换成json数据
        resp = json.loads(response)
        # 遍历
        for data in resp["aweme_list"]:
            # id值
            video_id = data['aweme_id']
            # 视频简介
            video_title = data['desc']
            # 构造视频网址
            video_url = 'https://www.iesdouyin.com/share/video/{}/?mid=1'
            # 填充内容
            video_douyin = video_url.format(video_id)
            print(video_id)
            print(video_title)
            print(video_douyin)


if __name__ == '__main__':
    douyin = Douyin()
    douyin.page_num()
