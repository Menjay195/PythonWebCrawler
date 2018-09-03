#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import requests
from urllib.parse import urlencode
 
def get_page(offset):
    params = {
        'offset': offset,
        'format': 'json',
        'keyword': '街拍',
        'autoload': 'true',
        'count': '20',
        'cur_tab': '1',
    }

    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
    }

    url = 'http://www.toutiao.com/search_content/?' + urlencode(params)
    try:
        response = requests.get(url,headers)
        if response.status_code == 200:
            return response.json()
    except requests.ConnectionError:
        return None

from collections import Iterable

def get_images(json):
    if json.get('data'):
        for item in json.get('data'):
            title = item.get('title')
            images = item.get('image_list')
            if isinstance(images, Iterable): 
                for image in images:
                    yield {
                        'image': 'http:'+image.get('url'),
                        'title': title
                    }

import os
from hashlib import md5
 
def save_image(item):
    if not os.path.exists(item.get('title')):
        os.mkdir(item.get('title'))
    try:
        response = requests.get(item.get('image').replace('list','large'))
        if response.status_code == 200:
            file_path = '{0}/{1}.{2}'.format(item.get('title'), md5(response.content).hexdigest(), 'jpg')
            if not os.path.exists(file_path):
                with open(file_path, 'wb') as f:
                    f.write(response.content)
            else:
                print('Already Downloaded', file_path)
    except requests.ConnectionError:
        print('Failed to Save Image')



from multiprocessing.pool import Pool

def main(offset):
    json = get_page(offset)
    for item in get_images(json):
        print(item)
        save_image(item)
  
# GROUP_START = 1
# GROUP_END = 5
 
# if __name__ == '__main__':
#     pool = Pool()
#     groups = ([x * 20 for x in range(GROUP_START, GROUP_END + 1)])
#     pool.map(main, groups)
#     pool.close()
#     pool.join()


if __name__ == '__main__':
    for i in range(1,3):
        main(i*20)
