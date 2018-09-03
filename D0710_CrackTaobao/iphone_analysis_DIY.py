#!/usr/bin/env python3
# -*- coding:utf-8 -*-

from selenium import webdriver
from urllib.parse import quote
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def get_html(page):
    keyword = 'iphone'
    url = 'https://s.taobao.com/search?q='+quote(keyword)
    browser = webdriver.Chrome()
    browser.get(url)
    if page > 1:
        wait = WebDriverWait(browser, 10)
        input = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#mainsrp-pager > div > div > div > div.form > input')))
        input.clear()
        input.send_keys(page)
        button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#mainsrp-pager > div > div > div > div.form > span.btn.J_Submit')))
        button.click()
    print(page)
    # print(type(browser.page_source))       #<class 'str'>
    return browser.page_source


from pyquery import PyQuery as pq
def get_products(content):
    doc = pq(content)

    #此方法选择失败
    # fetch = doc('#mainsrp-itemlist > div > div > div:nth-child(1)')
    # L = fetch.find('.item')
    # print(type(L))
    # L = L.items()
    # print(type(L))
    #参考，截取自浏览器开发者选项
    # //*[@id="mainsrp-itemlist"]/div/div/div[1]         #xpath
    #mainsrp-itemlist > div > div > div:nth-child(1)     #selector(伪类选择器)

    fetch = doc('#mainsrp-itemlist .items .item')
    print(type(fetch))
    L = fetch.items()
    print(type(L))

    L_save = []
    for item in L:
        product = [
            'http:'+item.find('.pic .img').attr('data-src'),   #'image'
            item.find('.price').text(),               #'price' 
            item.find('.deal-cnt').text(),            #'deal'
            item.find('.title').text(),               #'title'
            item.find('.shop').text(),                #'shop' 
            item.find('.location').text()             #'location' 
        ]
        print(product)
        L_save.append(product)
    return L_save


import csv
def save_to_CSV(data):
    with open('data.csv','w',encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['image','price','deal','title','shop','location'])
        writer.writerows(data)


if __name__ == '__main__':
    for page in range(1,2):
        content = get_html(page)
        data = get_products(content)
        save_to_CSV(data)

