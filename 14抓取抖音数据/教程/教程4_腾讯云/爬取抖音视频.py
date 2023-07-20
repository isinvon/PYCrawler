import requests
import json
import jsonpath


# 教程: https://cloud.tencent.com/developer/article/1936885#:~:text=Python%E7%88%AC%E5%8F%96%E6%8A%96%E9%9F%B3%E7%9F%AD%E8%A7%86%E9%A2%91%EF%BC%88%E6%97%A0%E6%B0%B4%E5%8D%B0%E7%89%88%EF%BC%89%201%201.%20%E4%BD%BF%E7%94%A8%E6%9B%B4%E7%AE%80%E5%8D%95%E7%9A%84%E6%96%B9%E6%B3%95%20%E5%9C%A8%E6%88%91%E4%B9%8B%E5%89%8D%E7%9A%84%E4%B8%80%E7%AF%87%E5%8D%9A%E5%AE%A2%E4%B8%AD%EF%BC%8C%E6%88%91%E7%94%A8%E4%BA%86%E6%9E%84%E9%80%A0%E7%BD%91%E5%9D%80%E7%9A%84%E6%96%B9%E6%B3%95%E6%9D%A5%E8%8E%B7%E5%8F%96%E6%8A%96%E9%9F%B3%E7%9F%AD%E8%A7%86%E9%A2%91%EF%BC%8C%E4%BD%86%E6%98%AF%E5%9C%A8%E4%BB%8A%E5%A4%A9%E6%88%91%E5%8F%88%E4%B8%80%E6%AC%A1%E7%9A%84%E7%A0%94%E7%A9%B6%E6%8A%96%E9%9F%B3%E7%9F%AD%E8%A7%86%E9%A2%91%E7%9A%84%E6%97%B6%E5%80%99%E5%8F%91%E7%8E%B0%E4%BA%86%E4%B8%80%E4%B8%AA%E6%9B%B4%E5%8A%A0%E7%AE%80%E5%8D%95%E7%9A%84%E6%96%B9%E6%B3%95%EF%BC%8C%E5%8F%91%E7%8E%B0%E6%88%91%E4%B9%8B%E5%89%8D%E7%9A%84%E5%88%86%E6%9E%90%E5%AE%9E%E5%9C%A8%E6%98%AF%E5%A4%AA%E8%BF%87%E7%B9%81%E7%90%90%E4%BA%86%EF%BC%8C%E6%89%80%E4%BB%A5%E6%9C%89%E5%86%99%E4%BA%86%E4%B8%80%E7%AF%87%E5%8D%9A%E5%AE%A2%E6%9D%A5%E8%AE%B0%E5%BD%95%E4%B8%8B%E8%BF%99%E4%B8%AA%E6%96%B9%E6%B3%95%E3%80%82%20%E4%B8%8E%E4%B8%8A%E4%B8%80%E7%AF%87%E5%8D%9A%E5%AE%A2%E4%B8%8D%E5%90%8C%E7%9A%84%E6%98%AF%EF%BC%8C%E8%BF%99%E4%B8%AA%E6%96%B9%E6%B3%95%E5%8F%AF%E4%BB%A5%E7%9C%81%E7%95%A5%E6%8E%89%E5%A4%A7%E9%87%8F%E7%9A%84%E5%88%86%E6%9E%90%E6%AD%A5%E9%AA%A4%20%E9%9A%8F%E4%BE%BF%E6%89%93%E5%BC%80%E4%B8%80%E4%B8%AA%E6%8A%96%E9%9F%B3%E4%B8%AA%E4%BA%BA%E4%B8%BB%E9%A1%B5%EF%BC%8C%E6%88%91%E9%80%89%E6%8B%A9%E7%9A%84%E6%98%AF%E7%88%B1%E5%A5%87%E8%89%BA%E4%BD%93%E8%82%B2%2C%E6%8E%A5%E7%9D%80%E5%8F%B3%E9%94%AE%E6%A3%80%E6%9F%A5%E7%BD%91%E9%A1%B5%E5%85%83%E7%B4%A0%EF%BC%8C%E7%82%B9%E5%87%BBnetwork%E9%80%89%E9%A1%B9%E5%8D%A1%E4%B8%8B%E7%9A%84xhr%E9%80%89%E9%A1%B9%EF%BC%8C%E5%88%86%E6%9E%90%E6%8A%93%E5%88%B0%E7%9A%84%E5%8C%85%20%E7%82%B9%E5%88%B0preview%E9%80%89%E9%A1%B9%E5%8D%A1%EF%BC%8C%E7%82%B9%E5%87%BBvideo-%3Edownload_addr-%3Eurl_list,4%204.%20%E4%B8%8D%E8%B6%B3%20...%205%205.%20%E4%BD%BF%E7%94%A8%E6%96%B9%E6%B3%95%20

class Douyin:
    def page_num(self, max_cursor):
        # 随机码
        random_field = '00nvcRAUjgJQBMjqpgesfdNJ72&dytk=4a01c95562f1f10264fb14086512f919'
        # 网址的主体
        url = 'https://www.iesdouyin.com/web/api/v2/aweme/post/?sec_uid=MS4wLjABAAAAU7Bwg8WznVaafqWLyLUwcVUf9LgrKGYmctJ3n5SwlOA&count=21&max_cursor=' + str(
            max_cursor) + '&aid=1128&_signature=' + random_field
        # 请求头
        headers = {
            'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36',
        }
        response = requests.get(url, headers=headers).text
        # 转换成json数据
        resp = json.loads(response)
        # 提取到max_cursor
        max_cursor = resp['max_cursor']
        # 遍历
        for data in resp['aweme_list']:
            # 视频简介
            video_title = data['desc']
            # 使用jsonpath语法提取paly_addr
            video_url = jsonpath.jsonpath(data, '$..paly_addr')
            for a in video_url:
                # 提取出来第一个链接地址
                video_realurl = a['url_list'][1]
            # 请求视频
            video = requests.get(video_realurl, headers=headers).content
            with open('t/' + video_title, 'wb') as f:
                print('正在下载：', video_title)
                f.write(video)

        # 判断停止构造网址的条件
        if max_cursor == 0:
            return 1
        else:
            douyin.page_num(max_cursor)


if __name__ == '__main__':
    douyin = Douyin()
    douyin.page_num(max_cursor=0)
