# -*- coding:utf-8 -*-
import urllib2
import re
import os
'''
Demo
http://www.xxxx.com/forumdata/backup_eec73d/100909_5q4T4Wp6-7.sql
'''
website="http://www.xxx.com/forumdata" #网站备份路径
webdir="/backup_eec73d/"                           #备份文件夹
fileqz="120418"                                    #备份日期（前缀）
filename="fz74JJpP"                                #8位 or 6位随机字符
filehz=".sql"
# 下载文件
def getFile(url):
    file_name = url.split('/')[-1]
    u = urllib2.urlopen(url)
    f = open(file_name, 'wb')
    block_sz = 8192
    while True:
        buffer = u.read(block_sz)
        if not buffer:
            break
        f.write(buffer)
    f.close()
    print "Sucessful to download" + " " + file_name
for url in range(1,39): #设置文件数
     url = website+webdir+fileqz+"_"+filename+"-"+str(url)+filehz    #获取完整文件地址
     getFile(url)    #下载文件
