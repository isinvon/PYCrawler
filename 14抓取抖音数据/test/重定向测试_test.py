# from django.shortcuts import redirect
#
# h = redirect('https://v.douyin.com/DG1j6FW/', permanent=True)
# print(h)

# from django.http import HttpResponseRedirect
#
# h = HttpResponseRedirect("http://www.baidu.com")
#
# print(h)

import urllib
from urllib import request
url = 'https://v.douyin.com/DG1j6FW/'

print(request.urlopen(url).geturl())