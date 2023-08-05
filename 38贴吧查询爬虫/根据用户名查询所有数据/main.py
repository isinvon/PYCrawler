import os,sys
from pathlib import Path
os.chdir(sys.path[0]) # 加上即可使用相对路径(解决相对路径问题)
# os.chdir() 方法用于改变当前工作目录到指定的路径。path-要切换到的新路径。

headers = {
    "user-agent":UserAgent().random
}
# 总站: https://ouotool.com/
# 接口
api = "https://ouotool.com/tb?un="
# 用户名
username = "username"

url = api + username
