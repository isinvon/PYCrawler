from matplotlib import pyplot as plt
import cv2
import os


# 滑动验证码工具: 'https://juejin.cn/post/6970289221038931976'
class SlideVerifyCode:
    def sovleCode(self):
        # （1）利用 cv2 将图片读取到程式中
        Dir = 'Downloads/'  # 目录
        path = Dir + 'filename.png'  # 文件路径
        if not os.path.exists(Dir):
            os.makedirs(Dir)

        image = cv2.imread(path)
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)  # Converting BGR to RGB
        plt.imshow(image)
        plt.show()

        # （2）判断图片中的物体边缘轮廓
        canny = cv2.Canny(image, 300, 300)
        plt.imshow(canny)
        plt.show()

        # （3）取出缺块所在的位置
        contours, hierarchy = cv2.findContours(canny, cv2.RETR_CCOMP, cv2.CHAIN_APPROX_SIMPLE)
        dx, dy = 0, 0
        for i, contour in enumerate(contours):
            x, y, w, h = cv2.boundingRect(contour)
            if (w > 50) and (h > 50):
                dx = x
                dy = y
            cv2.rectangle(image, (x, y), (x + w, y + h), (0, 0, 255), 2)

        plt.imshow(image)
        plt.show()

        # （1）打开浏览器前往网页，下载原始图片
        from selenium import webdriver
        from selenium.webdriver.support.ui import Select
        from selenium.webdriver.common.action_chains import ActionChains

        browser = webdriver.Edge('./chromedriver')

        js_download_code = '''
            var link = document.createElement('a');
            link.download = 'filename.png';
            link.href = document.getElementById('captcha').getElementsByTagName("canvas")[0].toDataURL()
            link.click();
        '''
        browser.execute_script(js_download_code)

        # 找出按钮元素
        btn = browser.find_element_by_class_name("jigsaw__slider--ihcNg")

        # （2）模拟使用者拖拉方块行为
        move = ActionChains(browser)
        move.click_and_hold(btn)
        move.move_by_offset(dx, 0)
        move.perform()
