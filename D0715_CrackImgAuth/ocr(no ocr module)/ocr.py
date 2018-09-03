#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import os
from PIL import Image

image = Image.open('code.jpg')
image = image.convert('L')
threshold = 127                    #值为127时等效于image = image.convert('1')
table = []
for i in range(256):
    if i < threshold:
        table.append(0)
    else:
        table.append(1)

image = image.point(table,'1')
# image.show()
newname = input('请为处理后的图片命名：\n')
image.save('%s.jpg'%newname)
os.system('tesseract %s.jpg result -l eng && cat result.txt'%newname)
