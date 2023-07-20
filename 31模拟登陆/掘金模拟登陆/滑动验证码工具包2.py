
# ① 利用 Python + opencv 拆解缺块位置
# 先手动把「背景图」下载到本地端电脑,再试着利用图像识别的方法试着找出位置.
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
from selenium import webdriver
from matplotlib import pyplot as plt

import cv2

# 第一步，我们先利用 cv2.imread(...) 把图片读到程式中，并且利用 cv2.cvtColor 进行颜色转换（原始图片有误差)：
path = '滑动验证码图片/滑动验证码背景图.png'
image = cv2.imread(path)
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)  # Converting BGR to RGB
plt.imshow(image)
plt.show()

#  Canny 方法能将原始图片转成灰阶之后，输出包含边缘范围的黑白影像：
canny = cv2.Canny(image, 300, 300)
plt.imshow(canny)
plt.show()

# 接下来利用 cv2.findContours() 找出图片中所有侦测到的区块，把他标记成蓝色的部分画出来。从长度（w）跟宽度（h）可以判断出哪一个区块是图片中真正的区块，但图片颜色太接近的情况下会增加判断的难度.
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

plt.imshow(image)
plt.show()


""" 利用 Python + Selenium 模拟滑动行为 """
browser = webdriver.Chrome('./chromedriver')

# 接下来利用 Selenium 打开浏览器跳转到网页中，利用 JavaScript 的先将 Canvas 转成图片后再进行下载 .
js_download_code = '''
    var link = document.createElement('a');
    link.download = 'filename.png';
    link.href = document.getElementById('captcha').getElementsByTagName("canvas")[0].toDataURL()
    link.click();
'''
browser.execute_script(js_download_code)

# 这么做就可以把原始图片下载下来，搭配「① 利用 Python + opencv 拆解缺块位置」可以得知需要移动的偏移量.


# 找到按钮元素
btn = browser.find_element_by_class_name("sc-kkGfuU bujTgx")


# （2）模拟使用者拖拉方块行为
move = ActionChains(browser)
move.click_and_hold(btn)
move.move_by_offset(dx, 0)
move.perform()
