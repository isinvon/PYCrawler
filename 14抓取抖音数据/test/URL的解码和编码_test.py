# coding=utf-8
import urllib
from urllib import parse

txt = '%e4%BD%A0%E5%A5%BD'
# URL解码
new_txt = urllib.parse.unquote(txt)
print(new_txt)
# URL编码
