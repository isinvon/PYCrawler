# -*-coding:utf8-*-
import os,sys
import re
import json
import time
import bs4
import pandas 
import urllib 
import requests
from fake_useragent import UserAgent #随机请求头库
from selenium import webdriver # 模拟用户操作
from msedge.selenium_tools import EdgeOptions  # 用于selenium无界面
from msedge.selenium_tools import Edge
from urllib import request  # 用于重定向
from colorama import Fore # 调色
from collections import Counter  # 用于统计
from prettytable import PrettyTable  # 美化表格的包
from pathlib import Path
os.chdir(sys.path[0]) # 加上即可使用相对路径(解决相对路径问题)
# os.chdir() 方法用于改变当前工作目录到指定的路径。path-要切换到的新路径。
from tkinter import *

win = Tk()
win.title("拜仁慕尼黑")

win.geometry('400x300')
# 创建一个文本控件
# width 一行可见的字符数；height 显示的行数
text = Text(win, width=50, height=20, undo=True, autoseparators=False)
text.grid()
# INSERT 光标处插入；END 末尾处插入
text.insert(INSERT, '这是一个GUI界面')
# 定义撤销和恢复方法，调用edit_undo()和 edit_redo()方法


def backout():
    text.edit_undo()


def regain():
    text.edit_redo()


# 定义撤销和恢复按钮
Button(win, text='撤销', command=backout).grid(
    row=3, column=0, sticky="w", padx=10, pady=5)
Button(win, text='恢复', command=regain).grid(
    row=3, column=0, sticky="e", padx=10, pady=5)
win.mainloop()

""" 作者：CeshirenTester
链接：https: // juejin.cn/post/7230257136700866616
来源：稀土掘金
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
 """