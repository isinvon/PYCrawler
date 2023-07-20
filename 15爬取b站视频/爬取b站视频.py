import json
import urllib
import re
import requests
import bs4
import pandas
import urllib3
# 因为b站的音频数据和视频画面是数据是分开的，需要用 ffmpeg 合成后才能得到我们要的视频。
import ffmpeg  # 用于合成音频的包
# 导入进程模块
import subprocess
# os模块是Python中整理文件和目录最为常用的模块
import os

# 教程链接: https://zhuanlan.zhihu.com/p/607349538
"""
提供信息:
    爬取的代码
    贪婪排序
    # reg = r'data-mp4="(.*?)"'
    # urllib.request.urlretrieve(i,"mp4/%s"%filename)
"""

# 爬取的视频主页
url = 'https://www.bilibili.com/video/BV1YV4y1K7pT'

# 视频的src
# url = "blob:https://www.bilibili.com/478de0da-a7c4-4c4d-9bbf-78de263509db"
# blob加密过的url需要解密,该方式展示丢弃

headers = {
    # 此处设置防盗链：指明连接的请求来源于B站，合法
    'referer': 'https://www.bilibili.com/',
    # 请求头是为了对python解析器进行伪装
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36 Edg/112.0.1722.64",
    # 给爬虫提供更多信息以抓取全
    "cookie": "buvid3=F9AE9251-1454-11B9-F71D-C624072C81A305376infoc; b_nut=1682573505; CURRENT_FNVAL=4048; bsource=search_bing; _uuid=12F62C10A-4663-B10AF-F9AC-3512ED139BE406116infoc; buvid4=8F43619B-B828-8137-7E10-2DFC4C07055606754-023042713-HiL283BrdD4rpmZdFCuAMg==; buvid_fp=268196c05f07750455249058d8a22b8f; CURRENT_PID=d0289ae0-e4bc-11ed-89de-855c6899af18; rpdid=|(~J~)Y~~Ju0J'uY)kl~Jluk; i-wanna-go-back=-1; FEED_LIVE_VERSION=V8; header_theme_version=CLOSE; home_feed_column=4; SESSDATA=0260e10b,1698212383,15372*42; bili_jct=23116a85dd5ea37cc4a5c6ec9de187b0; DedeUserID=446423825; DedeUserID__ckMd5=44b4dac40b10cd65; sid=8p3xyz76; b_ut=5; browser_resolution=1147-668; bp_video_offset_446423825=789974438767493200; nostalgia_conf=-1; innersign=1; b_lsid=FB471566_187CD2688A1",
}

# 模仿浏览器访问
response = requests.get(url=url, headers=headers)
# 返回相应码
status_code = response.status_code
# 获取网页源码
html = response.text
# 抓取视频标题
#   (加了?是非贪婪匹配,即只匹配某个词,不加?匹配就是贪婪匹配,匹配和这个词相关的所有字符串)
title = re.findall('<h1 title="(.*?)"', html)[0]
print('视频标题: ' + title + '\n' + '-------------------------------')
# 提取playinfo里面的数据
html_data = re.findall('<script>window.__playinfo__=(.*?)</script>', response.text)[0]
# html_data是json形式的,将其转成字典
json_data = json.loads(html_data)
'''
json.loads()：解析一个有效的JSON字符串并将其转换为Python字典
json.load()：从一个文件读取JSON类型的数据，然后转转换成Python字典
'''
# 让pycharm控制台以json格式化输出
# 不影响程序，只改变pycharm或vscode编辑器的终端输出显示
# indent=4 缩进4个空格
# 用dumps将python编码成json字符串
json_dicts = json.dumps(json_data, indent=4)
# 提取视频画面网址
video_url = json_data["data"]["dash"]["video"][0]["baseUrl"]
print("视频画面地址为：", video_url, '\n----------------------------------------')
audio_url = json_data["data"]["dash"]["audio"][0]["baseUrl"]
print("视频声音地址为: ", audio_url, '\n----------------------------------------')

# print(json_dicts)
# response.content获取响应体的二进制数据
video_content = requests.get(url=video_url, headers=headers).content
audio_content = requests.get(url=audio_url, headers=headers).content
print(type(video_content))

# 创建mp4文件,写入二进制数据
# if os.path.exists('视频文件夹'):
#     with open('视频文件夹\\' + title + '.mp4', mode='wb') as f:
#         f.write(vidio_content)
# else:
#     os.mkdir('视频文件夹')
#     with open('视频文件夹\\' + title + '.mp4', mode='wb') as f:
#         f.write(vidio_content)

# # 创建mp3文件,写入二进制数据
# if os.path.exists('视频文件夹'):
#     with open('视频文件夹\\' + title + '.mp3', mode='wb') as f:
#         f.write(audio_content)
# else:
#     os.mkdir('视频文件夹')
#     with open('视频文件夹\\' + title + '.mp3', mode='wb') as f:
#         f.write(audio_content)
# print("写入数据成功!", '\n----------------------------------------')
if (os.path.exists('视频文件夹')) == 'False':  # 如果文件夹不存在就创建
    os.mkdir("视频文件夹")  # 判断文件是否存在,不存在则自动创建
with open('视频文件夹\\' + title + '.mp4', mode='wb') as f:
    f.write(video_content)
with open('视频文件夹\\' + title + '.mp3', mode='wb') as f:
    f.write(audio_content)

# 合成视频
# ffmpeg -i video.mp4 -i audio.wav -c:v copy -c:a aac -strict experimental output.mp4
cmd = f"ffmpeg -i 视频文件夹\\{title}.mp4 -i 视频文件夹\\{title}.mp3 -c:v copy -c:a aac -strict experimental 视频文件夹\\{title}(最终版).mp4"
subprocess.run(cmd, shell=True)

print('恭喜你，视频合成成功！', '\n----------------------------------------')

# 删除不必要的画面和音频
os.remove(f'视频文件夹\\{title}.mp4')
os.remove(f'视频文件夹\\{title}.mp3')  # f其实就等价于format

print('程序结束...')

# 使用open读写文件的时候判断文件是否存在(不存在则创建):
'''
2. 在try块里面使用with open，然后捕获FileNotFoundError，使用os.mknod()函数创建文件，
    但是只适用于Linux，windows不能使用，因为windows下没有node概念。
    import os
     
    try:
        with open("test.txt",mode='r',encoding='utf-8') as ff:
            print(ff.readlines())
    except FileNotFoundError:
        os.mknod('test.txt')
        print("文件创建成功！")
-------------------------------------------------------------------------------
4. 不使用try块，使用os.path.exists()方法判断文件是否存在，如果不存在则创建文件。
    import os
    if os.path.exists('test.txt'):
        with open('test.txt',mode='r',encoding='utf-8') as ff:
            print(ff.readlines())
    else:
        with open("test.txt", mode='w', encoding='utf-8') as ff:
            print("文件创建成功！")
'''

# mode读取方式的知识点:
'''
教学导航: https://blog.csdn.net/weixin_48135624/article/details/114009667
rb模式：以字节(二进制)方式读取文件中的数据
wb模式: 以字节(二进制)方式往文件中写入数据
ab模式: 以字节(二进制)方式往文件末尾追加写入数据

ab模式表示往文件中追加写入字节数据，之前的历史数据会保留

学习rb模式的目的：
    1. 想要借助网络把一个文件中的数据发生给另外一个程序的话，需要使用字节(二进制)的数据
    2. 读取非文本文件，比如： 视频，图片，音频等文件需要使用rb模式读取数据
wb模式: 以字节(二进制)方式往文件中写入数据
    学习wb模式的使用场景：比如网络中接收的输入想要写入到文件，可以使用wb模式 
ab模式: 以字节(二进制)方式往文件末尾追加写入数据 
ab模式表示往文件中追加写入字节数据，之前的历史数据会保留   
'''
