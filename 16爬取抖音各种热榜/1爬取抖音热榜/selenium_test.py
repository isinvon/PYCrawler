# -*-coding:utf8-*-
import re
import os
import json
import bs4
import pandas
import requests
import unittest
from selenium import webdriver
from urllib import request  # 用于重定向
from colorama import Fore
import urllib
from collections import Counter  # 用于统计
from selenium.webdriver.common.by import By

# 参考: https://blog.csdn.net/hubing_hust/article/details/128295216

def test_eight_components():
    # 使用驱动实例开启会话
    driver = webdriver.Edge()

    driver.get("https://www.selenium.dev/selenium/web/web-form.html")

    title = driver.title
    assert title == "Web form"

    driver.implicitly_wait(0.5)

    text_box = driver.find_element(by=By.NAME, value="my-text")

    print(text_box)

    submit_button = driver.find_element(by=By.CSS_SELECTOR, value="button")

    text_box.send_keys("Selenium")
    submit_button.click()

    message = driver.find_element(by=By.ID, value="message")
    value = message.text
    assert value == "Received!"

    driver.quit()


if __name__ == '__main__':
    test_eight_components()
