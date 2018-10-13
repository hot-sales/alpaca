#!/usr/bin/python
from os import listdir
from os.path import isfile, join

imgpath = './img/'

imgs = [f for f in listdir(imgpath) if isfile(join(imgpath, f))]

# imgs = ['4871539221530_.pic.jpg', '4881539221531_.pic.jpg']

for img in imgs:
    print('<img src="img/%s" alt="hi" class="inline"/>\n' % img)

print('<img src="qrcode.jpg" alt="hi" class="inline"/>\n')
