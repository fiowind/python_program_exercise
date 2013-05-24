#!/usr/bin/python

import re
import urllib
import os

def getHtml(url):
    page = urllib.urlopen(url)
    html = page.read()
    return html

def getImg(html,file):
    reg = r'src="(.*?\.jpg)" width'
    imgre = re.compile(reg)
    imglist = re.findall(imgre,html)
    i=1
    for imgurl in imglist:
        urllib.urlretrieve(imgurl,'./%s/%s.jpg'%(file,i))
        i += 1
        

name = raw_input("print the name of file where you want to save:\n")
os.mkdir(name)
url = raw_input("url:\n")
print "Downloading..."
html = getHtml(url)
getImg(html,name)
print "Download ok!"