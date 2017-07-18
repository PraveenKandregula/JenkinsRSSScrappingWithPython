import urllib,urllib2
import base64
from bs4 import BeautifulSoup
import datetime
from datetime import date,timedelta
import re
import sys

ydate = str(datetime.date.today()-timedelta(1))
#ydate = str(datetime.date.today())
#print ydate

#This method formats credentials
def auth_headers(username, password):
   return 'Basic ' + base64.encodestring('%s:%s' % (username, password))[:-1]

#Credentials go here
auth = auth_headers(sys.argv[2], sys.argv[3])
#Home page url
homeUrl = sys.argv[1]
#RSS url
rssUrl = homeUrl+'/rssAll'
#This completes authentication and reads data from RSS url
req = urllib2.Request(rssUrl)
req.add_header('Authorization', auth)

#Fetching RSS feed
rssFeed = urllib2.urlopen(req).read()
#Formatting RSS feed to xml format
rssFeedXml = BeautifulSoup(rssFeed,"lxml")

#Extracting all entries from xml
entries =  rssFeedXml.find_all('entry')

print "Below jobs have run on date " +str(ydate)
#Iterating over all entries
for e in entries:
	#if ydate in e.find('published'):
	if re.search(str(ydate),str(e)):
		print e.find('title'),'\t',e.find('published'),'\n' 
