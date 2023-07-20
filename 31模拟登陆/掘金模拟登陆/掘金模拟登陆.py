# -*-coding:utf8-*-
import cv2
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
from http import cookies
import json
from lib2to3.pgen2 import driver
import os
import re
import sys
import time
from urllib import request, response
from webbrowser import Chrome
from PIL import Image, ImageChops

import bs4
import pyautogui
import requests
from sympy import false, true
import win32com.client
import win32con  # 系统操作
import win32gui
from matplotlib import pyplot as plt
from PIL import ImageGrab  # 操作图像
from pyscreeze import screenshot
from selenium import webdriver
# 用于截图的包
from win32gui import *  # 操作windows窗口

os.chdir(sys.path[0])  # 加上即可使用相对路径(解决相对路径问题)
# os.chdir() 方法用于改变当前工作目录到指定的路径。path-要切换到的新路径。
# 导入滑动验证码工具包
"""
需求: 模拟登陆掘金
思路: 使用token, 在每一次登陆完成之后获取新的token
思路2: selenium模拟用户点击鼠标然后登录, 中间验证码需要获取到本地,然后输入验证码真实的值即可
"""


class Imitatelogin:
    # 定义url, 账号, 密码, 验证码
    url = 'https://juejin.cn/'
    # url = 'https://juejin.cn/creator/home'  # 掘金创作者中心url
    username = '15677141741'
    password = 'linxinhuan123...'
    verifyCode = ''

    def selenium(self):  # 进行基础操作
        #  设置selenium无界面(无头模式)
        options = webdriver.ChromeOptions()
        options.use_chromium = True  # 是否开启浏览器可视化
        
        driver = webdriver.Chrome(
            executable_path='chromedriver.exe', options=options)  # 获得chrome浏览器的驱动
        # 让driver变成全局变量
        self.driver = driver
        driver.get(self.url)
        # 得到源码
        html = driver.page_source
        # 最大化浏览器
        driver.maximize_window()
        # 返回登录页面源码
        return html

    """ 微信登录 """

    def weichatLogin(self, cookies_flag):  # 微信二维码模拟登录掘金
        browser = self.driver
        # 判断本地是否有cookies可用
        if cookies_flag:  # 有cookies
            # 更新cookies后进入目标网页
            browser.get(self.url)
            page = browser.page_source
            print(page)
        else:  # 无cookies, 扫码登录
            # 点击登录头像
            browser.find_element_by_class_name('login-button').click()
            # # 等待框出现
            time.sleep(1)
            # 切换微信扫码登录
            browser.find_element_by_css_selector(
                '#juejin > div.global-component-box > div.auth-modal-box > form > div.auth-body > div.login-body > div.login-main > div.other-login-box > div > div > div:nth-child(2) > img'
            ).click()
            time.sleep(1)

    """ 账号密码登录 """

    def accountPasswordLogin(self, cookies_flag):  # 账号密码登录
        browser = self.driver
        # 判断本地是否有cookies可用
        if cookies_flag:  # 有cookies
            # 更新cookies后进入目标网页
            browser.get(self.url)
            page = browser.page_source
            print(page)
        else:  # 无cookies, 扫码登录
            time.sleep(1)
            # 点击登录头像
            browser.find_element_by_class_name('login-button').click()
            time.sleep(1)

            # 弹出登录框后点击使用密码登录
            browser.find_element_by_class_name('clickable').click()
            time.sleep(1)

            # 输入账号和密码
            browser.find_elements_by_name('loginPhoneOrEmail')[0].send_keys(
                self.username)  # 注意列表的时候element要加s不然报错‘WebElement‘ object is not subscriptable
            browser.find_elements_by_name('loginPassword')[
                0].send_keys(self.password)
            time.sleep(2)

            # 点击登录按钮
            browser.find_element_by_css_selector(
                '#juejin > div.global-component-box > div.auth-modal-box > form > div.auth-body > div.login-body > div.login-main > div.panel > button'
            ).click()
            time.sleep(5)
            # 点击登陆后出现滑动验证码
            # 调用滑动验证码函数解决

    def check_local_cookies_if_exists(self):  # 判断本地是否保存有cookies
        browser = self.driver
        # 判断本地是否保存有cookies
        filepath = '掘金登录cookies/掘金登录cookies.txt'
        if os.path.exists(filepath):  # 文件是存在
            if not os.path.getsize(filepath):  # 文件无内容
                print(filepath, " is empty!")  # 文件为空!
                return False
            else:  # 文件有内容
                with open(file=filepath, mode="r", encoding="utf-8") as f:
                    text = f.read()
                    listCookies = json.loads(text)
                for cookie in listCookies:
                    cookie_dict = {
                        # 'domain': 'wx.xxx.com',
                        'domain': cookie.get('domain'),
                        # 'expiry': cookie.get('expiry'),
                        # 'httpOnly': cookie.get('httpOnly'),
                        'name': cookie.get('name'),
                        'path': '/',
                        # 'sameSite': cookie.get('sameSite'),
                        'secure': cookie.get('secure'),
                        'value': cookie.get('value'),
                    }
                    f.close()
                    browser.add_cookie(cookie_dict=cookie_dict)  # 填充cookies
                print('---------cookies填充完毕----------')
                return True
        else:  # 文件不存在
            print('本地无cookies,需要进行扫码登陆或者密码登录(需要手动滑动验证码)')
            return False

    def get_cookies(self):  # 获取cookies保存本地
        # 获取cookies保存本地
        browser = self.driver
        dictCookies = browser.get_cookies()  # 获取list的cookies
        # print('---------------')
        # print(dictCookies)
        jsonCookies = json.dumps(dictCookies)  # 转换成字符串保存
        # print('---------------')
        # print(jsonCookies)
        if not os.path.exists('掘金登录cookies'):
            os.makedirs('掘金登录cookies')  # 创建文件夹
        with open(file="掘金登录cookies/掘金登录cookies.txt", mode="w", encoding="utf-8") as f:
            # 提前清空'掘金登录cookies.txt'的内容
            f.write(jsonCookies)
        f.close()
        print('---------cookies保存成功---------')
        print('=============登陆成功=============')

    def screenshot(self):  # 对微信二维码进行截图(已经弃用,因为调用需要时间, 等不到二维码被截屏的时候, 二维码已经被网页覆盖了)
        # 打开二维码图片
        if not os.path.exists('微信登录二维码'):
            os.makedirs('微信登录二维码')
        # selenium屏幕截图(得到二维码图片)
        # driver.get_screenshot_as_file('微信登录二维码/二维码.png')
        # 电脑屏幕截图
        screenshot = pyautogui.screenshot()
        screenshot.save('微信登录二维码/二维码.png')  # save screenshot
        screenshot.close()

        # 打开二维码图片
        img_path = r"微信登录二维码/二维码.png"
        img = plt.imread(img_path)
        # 创建图表'show picture'
        fig = plt.figure('show picture')
        # ax = fig.add_subplot(111)
        # 显示二维码
        plt.imshow(img)
        plt.show()
        # 关闭图片显示
        plt.close()

    def download_slide_VerifyCode(self):
        browser = self.driver
        # 下载验证码的背景图到本地
        if not os.path.exists('ImgVerifyCode'):
            os.makedirs('ImgVerifyCode')  # 创建文件夹

        # ---获取验证码背景图的url
        verifyCode_imgBackground_url = browser.find_element_by_id('captcha-verify-image').get_attribute('src')  # 用get_attribute获取属性对应的属性值
        # 将获取到的图片二进制流写入本地文件
        r1 = requests.get(verifyCode_imgBackground_url).content
        # 对于图片类型的通过r.content方式访问响应内容，将响应内容写baidu.png中f.write(r.content)
        with open('ImgVerifyCode/verifyCode_imgBackground.png', 'wb') as f:
            f.write(r1)  # 将图片的二进制数据流写入文件
            f.close()
        print('----下载完成图片1: ' + str(verifyCode_imgBackground_url))
        time.sleep(1)
        # ---获取验证码拖动块的url
        verifyCode_imgBlock_url = browser.find_element_by_xpath('//*[@id="captcha_container"]/div/div[2]/img[2]').get_attribute("src")
        # 将获取到的图片二进制流写入本地文件
        r2 = requests.get(verifyCode_imgBlock_url).content
        # 对于图片类型的通过r.content方式访问响应内容，将响应内容写baidu.png中f.write(r.content)
        with open('ImgVerifyCode/verifyCode_imgBlock.png', 'wb') as f:
            f.write(r2)  # 将图片的二进制数据流写入文件
            f.close()
        print('---下载完成图片2: ' + str(verifyCode_imgBlock_url))

    def sovle_slide_VerifyCode1(self):  # 解决滑动验证码方案1
        browser = self.driver
        # ① 利用 Python + opencv 拆解缺块位置
        # 先手动把「背景图」下载到本地端电脑,再试着利用图像识别的方法试着找出位置.
        path = 'ImgVerifyCode/verifyCode_imgBackground.png'
        image = cv2.imread(path)
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)  # Converting BGR to RGB
        plt.imshow(image)
        plt.show()

        canny = cv2.Canny(image, 300, 300)
        plt.imshow(canny)
        plt.show()

        contours, hierarchy = cv2.findContours(
            canny, cv2.RETR_CCOMP, cv2.CHAIN_APPROX_SIMPLE)
        dx, dy = 0, 0
        for i, contour in enumerate(contours):
            x, y, w, h = cv2.boundingRect(contour)
            if (w > 50) and (h > 50):
                # 最终就可以得到缺块所在的位置是 dx 和 dy 两个变数：
                dx = x
                dy = y
            cv2.rectangle(image, (x, y), (x + w, y + h), (0, 0, 255), 2)
        print('-----------------')
        print(f'验证码背景缺口坐标x:{dx}  y:{dy}')
        plt.imshow(image)
        plt.show()

        # 利用 Python + Selenium 模拟滑动行为

        # 这么做就可以把原始图片下载下来，搭配「① 利用 Python + opencv 拆解缺块位置」可以得知需要移动的偏移量.
        # 找到按钮元素
        # btn = browser.find_element_by_id("verify-points")
        btn = browser.find_element_by_xpath('//*[@id="captcha_container"]/div/div[2]/img[2]')
        # （2）模拟使用者拖拉方块行为
        move = ActionChains(browser)
        move.click_and_hold(btn)
        move.move_by_offset(dx, 0)  # 往右偏移dx个像素
        move.release()  # 释放鼠标
        move.perform()

    def sovle_slide_VerifyCode2(self):  # 解决滑动验证码方案2
        browser = self.driver
        # 定位滑块
        slide_btn = browser.find_element_by_xpath('//*[@id="captcha_container"]/div/div[2]/img[2]')
        # 定位背景图
        pre_img = browser.find_element_by_id('captcha-verify-image')
        # 截取背景图
        pre_img.screenshot('before.png')
        time.sleep(1)
        # 使用js隐藏方块
        script = """
            var missblock = document.getElementById('missblock');
            missblock.style['visibility'] = 'hidden';
        """
        browser.execute_script(script)
        time.sleep(1)
        # 再次截图
        pre_img.screenshot('after.png')

        # 使用PIL创建Image
        before_img = Image.open('before.png').convert('RGB')
        after_img = Image.open('after.png').convert('RGB')
        # 使用ImageChops对比差异
        different_place = ImageChops.difference(before_img, after_img)
        diff_position = different_place.getbbox()

        # 使用js显示方块
        script = """
            var missblock = document.getElementById('missblock');
            missblock.style['visibility'] = '';
        """
        browser.execute_script(script)
        time.sleep(1)
        # 事件对象
        actionChains = ActionChains(browser)
        # 点击滑块
        actionChains.click_and_hold(slide_btn).perform()
        # 观察网站滑块移动的长度和位置
        actionChains.drag_and_drop_by_offset(slide_btn, diff_position[0] - 10, 0)
        actionChains.release()
        actionChains.perform()
        time.sleep(2)

    def sovle_slide_VerifyCode3(self):  # 解决滑动验证码方案3
        global x
        browser = self.driver
        path = 'ImgVerifyCode/verifyCode_imgBackground.png'
        image = cv2.imread(path)  # cv2的路径不能有中文
        blurred = cv2.GaussianBlur(image, (5, 5), 0)
        cv2.imshow('blurred', blurred)
        canny = cv2.Canny(blurred, 200, 400)
        cv2.imshow("canny", canny)

        contours, hierarchy = cv2.findContours(canny, cv2.RETR_CCOMP, cv2.CHAIN_APPROX_SIMPLE)
        for i, contours in enumerate(contours):
            x, y, w, h = cv2.boundingRect(contours)
            cv2.rectangle(image, (x + w, y + h), (0, 0, 255), 2)
        dx = x
        cv2.imshow("image", image)
        # 找到按钮元素
        # btn = browser.find_element_by_id("verify-points")
        btn = browser.find_element_by_class_name("sc-kkGfuU bujTgx")
        # （2）模拟使用者拖拉方块行为
        # 事件对象
        actionChains = ActionChains(browser)
        # 点击滑块
        actionChains.click_and_hold(btn)
        # 观察网站滑块移动的长度和位置
        actionChains.drag_and_drop_by_offset(btn, dx, 0)
        actionChains.release()
        actionChains.perform()
        time.sleep(2)

    def get_html(self):  # 对登录之后的页面获取源码
        response = requests.get()


if __name__ == '__main__':
    loginObject = Imitatelogin()
    """ 进行基础操作 """
    loginObject.selenium()
    """ 判断本地是否存在cookies, 并且返回一个boolean供使用 """
    cookies_flag = loginObject.check_local_cookies_if_exists()
    """ 微信登录 """
    # loginObject.weichatLogin(cookies_flag)
    # 密码登录
    loginObject.accountPasswordLogin(cookies_flag)
    # 获取(下载)密码登录后的ImgVerifyCode
    loginObject.download_slide_VerifyCode()
    time.sleep(2)
    # 拖动验证码
    loginObject.sovle_slide_VerifyCode2()
    """ 登录之后获取cookies保存到本地 """
    loginObject.get_cookies()
    # 结束浏览器工作
    time.sleep(10)
    # loginObject.driver.quit()
