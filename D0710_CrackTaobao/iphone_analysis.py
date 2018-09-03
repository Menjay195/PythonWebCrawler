#!/usr/bin/env python3
# -*- coding:utf-8 -*-

from selenium import webdriver
from urllib.parse import quote
import time

def get_html(page):
    keyword = 'iphone'
    url = 'https://s.taobao.com/search?q='+quote(keyword)
    browser = webdriver.Chrome()
    browser.get(url)
    if page > 1:
        time.sleep(10)
        input = browser.find_element_by_css_selector("#mainsrp-pager > div > div > div > div.form > input")
        input.clear()
        input.send_keys(page)
        button = browser.find_element_by_css_selector("#mainsrp-pager > div > div > div > div.form > span.btn.J_Submit")
        button.click()
    print(page)


for i in range(1,6):
    get_html(i)

