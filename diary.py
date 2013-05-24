#!/usr/bin/env python
import sys,time,os

shijian = time.strftime('%Y-%m-%d  %H:%M',time.localtime(time.time()))
fileName = raw_input ("Please input your file name:\n")
myfile = open (fileName+'.txt','a+')

if os.path.isfile(os.getcwd()+'/'+fileName+'.txt'):
    print 'The file exist,do you want to show the content before?(y/n)'
    yn = raw_input()
    if yn=='y':
        print myfile.read()
        
else:
    print 'A new txt file builded!'
print "Please input your content:\n(print'exit'to exit,\nprint cancel to cancel)\n"+shijian

i=1
for line in sys.stdin:
    if i==1:
        if line.strip()=='cancel':
            break
        else:
            myfile.write(shijian+'\n')
    if line.strip()=='exit' :
        break
    myfile.write(line)
    i=i+1
myfile.close()
