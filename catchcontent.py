#!/usr/bin/python
# -*- coding: utf-8 -*-

import urllib2, httplib, urlparse
import re, os
import HTMLParser
import time


fin = open("./ycinput.txt", mode='r')
data = fin.read()
fout = open("./output_action2.txt", mode='w')


def openwenzhang():
	reg1 = re.compile(r'查看文章<a href="(.*?)">')
	reg2 = re.compile(r'<div class=\\"WB_innerwrap\\">([\d\D]*)<script>FM.view\({"ns":"pl.content')
	reg3 = re.compile(r'replace\("(.*?)"\);')
	# reg1 = reg1.decode('gbk')
	yuanchuang = reg1.findall(data)
	for url in yuanchuang:
		html_parser = HTMLParser.HTMLParser()
		url = html_parser.unescape(url) 
		# print url
		req = urllib2.Request(url)
		req.add_header("User-Agent", "Mozilla/5.0 (X11; Linux x86_64; rv:36.0) Gecko/20100101 Firefox/36.0")
		req.add_header("Cookie", "SUB=_2A254gn2FDeTxGedM71IS9i7EzD-IHXVbjQPNrDV6PUNbvtBeLU_akW1zsXw2RDF9Def_fvdNGBr7WCWA-w..; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WWnbKu9EEBeo28P3P8dhTo95JpX5KMt; SUHB=0XDk1CyX5ubFTP; SSOLoginState=1434848725; _T_WM=134f7e71de35b1024ea4cbb891069032")
		req.add_header('Accept-Encoding', 'utf-8')
		try:
			res = urllib2.urlopen(req)
			print 'ok1'
		except:
			print 'error open'
			continue
		html = res.read()
		realurl = reg3.findall(html)
		realurl = realurl[0]
		print realurl
		req = urllib2.Request(realurl)
		req.add_header("User-Agent", "Mozilla/5.0 (X11; Linux x86_64; rv:36.0) Gecko/20100101 Firefox/36.0")
		req.add_header("Cookie", "	SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WWnbKu9EEBeo28P3P8dhTo9; SINAGLOBAL=222.243.110.190_1420459210.19736; U_TRS1=000000e2.b5a27b87.54afd8e0.b60cf8ed; UOR=s.weibo.com,qing.blog.sina.com.cn,; ULV=1422249483553:4:4:1:222.243.110.177_1422246552.341568:1422086337267; __utma=269849203.558097129.1420810492.1420810492.1420810492.1; __utmz=269849203.1420810492.1.1.utmcsr=s.weibo.com|utmccn=(referral)|utmcmd=referral|utmcct=/weibo/kindle%2520%25E8%25B5%2584%25E6%25BA%2590; vjuids=d06bf292d.14acee81d31.0.27ec531526cb1; vjlast=1422249490.1422251651.10; SGUID=1420810527185_63972545; sso_info=v02m6alo5qztYaalr2fnbalrpmCmbWalpC9jJOItIyDjLaMg6C3jLDAwA==; ALF=1466384724; SUS=SID-1240360873-1434848724-GZ-mhwke-9774ddddeb4362c6ac03ae940c82c763; SUE=es%3D8867f8d8f5c8ae27db289ecaa5009350%26ev%3Dv1%26es2%3Dd319cfa53489a3eab44cabfadcb95b20%26rs0%3DDNBRBCQXXHo9ur631OU%252FT%252BzV8BPYs40Vtk4x3ZrtJ86EXdUoQL3PTTJNx2JnHn0oK8qQJGG6qObV9ioMI%252BN7W8UQESUtiV%252FU5Zbl8QLmd3boQZrluek3RtD%252Biac9So3Z0Ua4s%252FWfk7PNsQFz%252FL24MKeNahnl2Ox%252BX3FG1mmXR%252BY%253D%26rv%3D0; SUP=cv%3D1%26bt%3D1434848724%26et%3D1434935124%26d%3D40c3%26i%3Dc763%26us%3D1%26vf%3D0%26vt%3D0%26ac%3D43%26st%3D0%26lt%3D7%26uid%3D1240360873%26user%3D%25E5%2591%25A8%25E8%258A%25B3%25E6%2598%259F%26ag%3D2%26name%3D%25E5%2591%25A8%25E8%258A%25B3%25E6%2598%259F%26nick%3DFio_wind%26sex%3D2%26ps%3D0%26email%3D%26dob%3D1991-12-26%26ln%3D%26os%3D%26fmp%3D%26lcp%3D2012-12-22%252022%253A56%253A11; SUB=_2A254gn2EDeTxGedM71IS9i7EzD-IHXVb9uhMrDV_PUNbvtBeLUrwkW9b1IOpeIa_ItZ89uzZeDgnnqViyQ..; Apache=58.33.232.17_1434852004.957519")
		req.add_header('Accept-Encoding', 'utf-8')
		try:
			res = urllib2.urlopen(req)
			print 'ok2'
		except:
			print 'error open'
			continue
		html = res.read()
		# print html
		wenzhang = reg2.findall(html)
		if not wenzhang:
			print 'reg none'
			continue
		print wenzhang[0]
		fout.write(wenzhang[0]+'\n\n')


def catchweibo():
	c = 3362
	# c是爬虫起始页
	for i in range(6906):
		pn = (i+c)
		url = 'http://weibo.cn/1767797335/profile?filter=0&page='+str(pn)	
		#上面地址是你要爬的人的微薄url，用weibo.cn访问限制少	
		print url
		req = urllib2.Request(url)
		req.add_header("User-Agent", "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.101 Safari/537.36")
		req.add_header("Cookie", "_T_WM=edf4469bb5245a50aa32006460daa5ae; _T_WL=1; _WEIBO_UID=5638019231; SUB=_2A254gp9aDeTxGeNI6FoR8SfOyD2IHXVbjCESrDV6PUJbrdAKLXOnkW1HSRVVWhAfa6SQUOfsMJvV5z1nWg..; gsid_CTandWM=4u3Fdd4a1W8HT0Rlp91lUnEHN3J")
		#上面这行修改自己的cookie，每个cookie大概能爬1000页左右，如果只有一个帐号就隔一个小时之后再爬
		try:
			res = urllib2.urlopen(req)
			print 'ok1'
		except:
			print 'error open'
			continue
		html = res.read()
		print html

		reg1 = re.compile(r'(<div class="c" id="M_[\d\D]*?)<div class="s"></div>')
		reg2 = re.compile(r'<span class="ct">(.*?)&nbsp;')
		yuanchuang = reg1.findall(html)
		# atime = reg2.findall(html)
		if not yuanchuang:
			print 'reg none'
			c = c-1
			continue
		for j in range(0, len(yuanchuang)):
			print len(yuanchuang)
			print yuanchuang[j]
			print '\n'
			fout.write(yuanchuang[j]+'\n'+'\n<br><br>')
		# time.sleep(0.3)


catchweibo()
# openwenzhang() #这个是用来爬文章的

fout.close()
fin.close()
