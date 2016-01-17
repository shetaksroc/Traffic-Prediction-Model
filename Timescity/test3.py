import MySQLdb
import csv
import urllib2, urllib
#db = MySQLdb.connect(host="localhost",user="root",passwd="",db="db2")
#cur = db.cursor()
reader=csv.reader(open('event.csv','rb'))
#query = """INSERT INTO mytable (event,type,place,place1,date,time) VALUES (%s, %s, %s, %s, %s, %s)"""
for row in reader:
	event=row[0]
	type=row[1]
	place=row[2]
	place1=row[3]
	date=row[4]
	time=row[5]
	if(event=="event"):
		continue



mydata={'event':'hi','type':'hello','place':'good','place1':'ille','date':'ivathe','time':'igale'}   #The first is the var name the second is the value
mydata=urllib.urlencode(mydata)
path='http://tdapp.webuda.com/insertpy.php'   #the url you want to POST to
req=urllib2.Request(path, mydata)
req.add_header("Content-type", "application/x-www-form-urlencoded")
page=urllib2.urlopen(req).read()
print page