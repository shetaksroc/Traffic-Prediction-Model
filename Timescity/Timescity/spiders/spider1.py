from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector
from scrapy.selector import Selector
from Timescity.items import TimescityItem
import scrapy

class MySpider1(BaseSpider):
	name = "MySpider1"
	allowed_domains = ["timescity.com"]
	start_urls = ["http://timescity.com/bangalore/events"]
	
	def parse(self,response):
		hxs = HtmlXPathSelector(response)
		#date = hxs.select("//div[@id='exp_first']/span/span[@class='c_date black']/text()").extract()
		event = hxs.select("//li[@class='evnt_name']/a/text()").extract()
		type = hxs.select("//li/a[@class='evtnm_h font11']/text()").extract()
		place = hxs.select("//li[@class='gry_txt_drk']/a[@class='black']/text()").extract()
		time = hxs.select("//li[@class='gry_txt_drk timex']/text()").extract()
		#ur = []
		print event
		print 
		print 
		print type
		print 
		print 
		print place
		print
		print 
		print time
		
items = []
import csv

class MySpider2(BaseSpider):
	name = "MySpider2"
	allowed_domains = ["timescity.com"]
	start_urls = ["http://timescity.com/bangalore/events"]
	c = csv.writer(open("event.csv", "ab"))
	
	def parse(self,response):
		hxs = Selector(response)
		date = hxs.xpath("//div[@id='exp_first']/span/span[@class='c_date black']/text()").extract()
		event = hxs.xpath("//div[@id='exp_first']//li[@class='evnt_name']/a/text()").extract()
		type = hxs.xpath("//div[@id='exp_first']//li/a[@class='evtnm_h font11']/text()").extract()
		place = hxs.xpath("//div[@id='exp_first']//li[@class='gry_txt_drk']/a[@class='black']/text()").extract()
		time = hxs.xpath("//div[@id='exp_first']//li[@class='gry_txt_drk timex']/text()").extract()
		#ur = []
		'''print date
		print event
		print type
		print place
		print time'''
		#items=[]
		l=len(event)
		self.c.writerow(["event","type","place","place1","date","time"])
		global items
		j=0
		for i in range(l):
			self.c.writerow([event[i],type[i],place[j],place[j+1],date[0],time[i]])
			j+=2
		'''for i in range(l):
			item = TimescityItem()
			item["date"] = date
			item["event"] = event[i]
			item["type"] = type[i]
			item["place"] = place[j]
			item["place1"] = place[j+1]
			j+=2
			item["time"] = time[i]
			items.append(item)
		return items'''

class MySpider3(BaseSpider):
	name = "MySpider3"
	allowed_domains = ["timescity.com"]
	start_urls = ["http://timescity.com/bangalore/events"]
	c = csv.writer(open("event.csv", "ab"))
	
	def parse(self,response):
		hxs = Selector(response)
		id = ["exp_first","exp_second","exp_third","exp_fourth","exp_fifth","exp_sixth","exp_seventh"]
		#for i in id:
		date = hxs.xpath("//div[@id='exp_second']/span/span[@class='c_date black']/text()").extract()
		event = hxs.xpath("//div[@id='exp_second']//li[@class='evnt_name']/a/text()").extract()
		type = hxs.xpath("//div[@id='exp_second']//li/a[@class='evtnm_h font11']/text()").extract()
		place = hxs.xpath("//div[@id='exp_second']//li[@class='gry_txt_drk']/a[@class='black']/text()").extract()
		place1 = hxs.xpath("//div[@id='exp_second']//li[@class='gry_txt_drk']/span[@class='locality_name']/a/text()").extract()
		time = hxs.xpath("//div[@id='exp_second']//li[@class='gry_txt_drk timex']/text()").extract()
		#ur = []
		'''print date
		print event
		print type
		print place
		print place1
		print time'''
		#self.c.writerow(["event","type","place","place1","date","time"])
		#items=[]
		global items
		l=len(event)
		for i in range(l):
			self.c.writerow([event[i],type[i],place[i],place1[i],date[0],time[i]])
		'''for i in range(l):
			item = TimescityItem()
			item["date"] = date
			item["event"] = event[i]
			item["type"] = type[i]
			item["place"] = place[i]
			item["place1"] = place1[i]
			item["time"] = time[i]
			items.append(item)
		return items'''
		
	
class MySpider4(BaseSpider):
	name = "MySpider4"
	allowed_domains = ["timescity.com"]
	start_urls = ["http://timescity.com/bangalore/events"]
	c = csv.writer(open("event.csv", "ab"))
	
	def parse(self,response):
		hxs = Selector(response)
		id = ["exp_first","exp_second","exp_third","exp_fourth","exp_fifth","exp_sixth","exp_seventh"]
		#for i in id:
		date = hxs.xpath("//div[@id='exp_third']/span/span[@class='c_date black']/text()").extract()
		event = hxs.xpath("//div[@id='exp_third']//li[@class='evnt_name']/a/text()").extract()
		type = hxs.xpath("//div[@id='exp_third']//li/a[@class='evtnm_h font11']/text()").extract()
		place = hxs.xpath("//div[@id='exp_third']//li[@class='gry_txt_drk']/a[@class='black']/text()").extract()
		place1 = hxs.xpath("//div[@id='exp_third']//li[@class='gry_txt_drk']/span[@class='locality_name']/a/text()").extract()
		time = hxs.xpath("//div[@id='exp_third']//li[@class='gry_txt_drk timex']/text()").extract()
		#ur = []
		'''print date
		print event
		print type
		print place
		print place1
		print time'''
		#items=[]
		global items
		l=len(event)
		for i in range(l):
			self.c.writerow([event[i],type[i],place[i],place1[i],date[0],time[i]])
		'''for i in range(l):
			item = TimescityItem()
			item["date"] = date[0]
			item["event"] = event[i]
			item["type"] = type[i]
			item["place"] = place[i]
			item["place1"] = place1[i]
			item["time"] = time[i]
			items.append(item)
		return items'''
		
class MySpider5(BaseSpider):
	name = "MySpider5"
	allowed_domains = ["timescity.com"]
	start_urls = ["http://timescity.com/bangalore/events"]
	c = csv.writer(open("event.csv", "ab"))
	
	def parse(self,response):
		hxs = Selector(response)
		id = ["exp_first","exp_second","exp_third","exp_fourth","exp_fifth","exp_sixth","exp_seventh"]
		#for i in id:
		date = hxs.xpath("//div[@id='exp_fourth']/span/span[@class='c_date black']/text()").extract()
		event = hxs.xpath("//div[@id='exp_fourth']//li[@class='evnt_name']/a/text()").extract()
		type = hxs.xpath("//div[@id='exp_fourth']//li/a[@class='evtnm_h font11']/text()").extract()
		place = hxs.xpath("//div[@id='exp_fourth']//li[@class='gry_txt_drk']/a[@class='black']/text()").extract()
		place1 = hxs.xpath("//div[@id='exp_fourth']//li[@class='gry_txt_drk']/span[@class='locality_name']/a/text()").extract()
		time = hxs.xpath("//div[@id='exp_fourth']//li[@class='gry_txt_drk timex']/text()").extract()
		#ur = []
		'''print date
		print event
		print type
		print place
		print place1
		print time'''
		#items=[]
		global items
		l=len(event)
		for i in range(l):
			self.c.writerow([event[i],type[i],place[i],place1[i],date[0],time[i]])
		'''for i in range(l):
			item = TimescityItem()
			item["date"] = date[0]
			item["event"] = event[i]
			item["type"] = type[i]
			item["place"] = place[i]
			item["place1"] = place1[i]
			item["time"] = time[i]
			items.append(item)
		return items'''
		
class MySpider6(BaseSpider):
	name = "MySpider6"
	allowed_domains = ["timescity.com"]
	start_urls = ["http://timescity.com/bangalore/events"]
	c = csv.writer(open("event.csv", "ab"))
	
	def parse(self,response):
		hxs = Selector(response)
		id = ["exp_first","exp_second","exp_third","exp_fourth","exp_fifth","exp_sixth","exp_seventh"]
		#for i in id:
		date = hxs.xpath("//div[@id='exp_fifth']/span/span[@class='c_date black']/text()").extract()
		event = hxs.xpath("//div[@id='exp_fifth']//li[@class='evnt_name']/a/text()").extract()
		type = hxs.xpath("//div[@id='exp_fifth']//li/a[@class='evtnm_h font11']/text()").extract()
		place = hxs.xpath("//div[@id='exp_fifth']//li[@class='gry_txt_drk']/a[@class='black']/text()").extract()
		place1 = hxs.xpath("//div[@id='exp_fifth']//li[@class='gry_txt_drk']/span[@class='locality_name']/a/text()").extract()
		time = hxs.xpath("//div[@id='exp_fifth']//li[@class='gry_txt_drk timex']/text()").extract()
		#ur = []
		'''print date
		print event
		print type
		print place
		print place1
		print time'''
		#items=[]
		global items
		l=len(event)
		for i in range(l):
			self.c.writerow([event[i],type[i],place[i],place1[i],date[0],time[i]])
		'''for i in range(l):
			item = TimescityItem()
			item["date"] = date[0]
			item["event"] = event[i]
			item["type"] = type[i]
			item["place"] = place[i]
			item["place1"] = place1[i]
			item["time"] = time[i]
			items.append(item)
		return items'''
		
class MySpider7(BaseSpider):
	name = "MySpider7"
	allowed_domains = ["timescity.com"]
	start_urls = ["http://timescity.com/bangalore/events"]
	c = csv.writer(open("event.csv", "ab"))
	
	def parse(self,response):
		hxs = Selector(response)
		id = ["exp_first","exp_second","exp_third","exp_fourth","exp_fifth","exp_sixth","exp_seventh"]
		#for i in id:
		date = hxs.xpath("//div[@id='exp_sixth']/span/span[@class='c_date black']/text()").extract()
		event = hxs.xpath("//div[@id='exp_sixth']//li[@class='evnt_name']/a/text()").extract()
		type = hxs.xpath("//div[@id='exp_sixth']//li/a[@class='evtnm_h font11']/text()").extract()
		place = hxs.xpath("//div[@id='exp_sixth']//li[@class='gry_txt_drk']/a[@class='black']/text()").extract()
		place1 = hxs.xpath("//div[@id='exp_sixth']//li[@class='gry_txt_drk']/span[@class='locality_name']/a/text()").extract()
		time = hxs.xpath("//div[@id='exp_sixth']//li[@class='gry_txt_drk timex']/text()").extract()
		#ur = []
		'''print date
		print event
		print type
		print place
		print place1
		print time'''
		#items=[]
		global items
		l=len(event)
		for i in range(l):
			self.c.writerow([event[i],type[i],place[i],place1[i],date[0],time[i]])
		'''for i in range(l):
			item = TimescityItem()
			item["date"] = date[0]
			item["event"] = event[i]
			item["type"] = type[i]
			item["place"] = place[i]
			item["place1"] = place1[i]
			item["time"] = time[i]
			items.append(item)
		return items'''
		
class MySpider8(BaseSpider):
	name = "MySpider8"
	allowed_domains = ["timescity.com"]
	start_urls = ["http://timescity.com/bangalore/events"]
	c = csv.writer(open("event.csv", "ab"))
	
	def parse(self,response):
		hxs = Selector(response)
		id = ["exp_first","exp_second","exp_third","exp_fourth","exp_fifth","exp_sixth","exp_seventh"]
		#for i in id:
		date = hxs.xpath("//div[@id='exp_seventh']/span/span[@class='c_date black']/text()").extract()
		event = hxs.xpath("//div[@id='exp_seventh']//li[@class='evnt_name']/a/text()").extract()
		type = hxs.xpath("//div[@id='exp_seventh']//li/a[@class='evtnm_h font11']/text()").extract()
		place = hxs.xpath("//div[@id='exp_seventh']//li[@class='gry_txt_drk']/a[@class='black']/text()").extract()
		place1 = hxs.xpath("//div[@id='exp_seventh']//li[@class='gry_txt_drk']/span[@class='locality_name']/a/text()").extract()
		time = hxs.xpath("//div[@id='exp_seventh']//li[@class='gry_txt_drk timex']/text()").extract()
		#ur = []
		'''print date
		print event
		print type
		print place
		print place1
		print time'''
		#items=[]
		global items
		l=len(event)
		for i in range(l):
			self.c.writerow([event[i],type[i],place[i],place1[i],date[0],time[i]])
		'''for i in range(l):
			item = TimescityItem()
			item["date"] = date[0]
			item["event"] = event[i]
			item["type"] = type[i]
			item["place"] = place[i]
			item["place1"] = place1[i]
			item["time"] = time[i]
			items.append(item)
		return items'''
		
		
		
class MySpider9(BaseSpider):
	name = "MySpider9"
	allowed_domains = ["www.buzzintown.com"]
	start_urls = ["http://www.buzzintown.com/bangalore/events/category--music-concerts+nightlife+sports-outdoor+theatre-arts/day--tomorrow+thisweekend+nextweekend.html"]
	#"http://www.buzzintown.com/bangalore/events/category--music-concerts+nightlife+sports-outdoor+theatre-arts/day--tomorrow+thisweekend+nextweekend.html/page--2.html",
	#"http://www.buzzintown.com/bangalore/events/category--music-concerts+nightlife+sports-outdoor+theatre-arts/day--tomorrow+thisweekend+nextweekend.html/page--3.html",
	#"http://www.buzzintown.com/bangalore/events/category--music-concerts+nightlife+sports-outdoor+theatre-arts/day--tomorrow+thisweekend+nextweekend.html/page--4.html"]
	c=csv.writer(open("event.csv","ab"))
	#c.writerow(["event","type","place","place1","date"])
	#hxs = Selector("http://www.buzzintown.com/bangalore/events/category--music-concerts+nightlife+sports-outdoor+theatre-arts/day--tomorrow+thisweekend+nextweekend.html")
	ur = []
	
	def parse(self,response):
		hxs = Selector(response)
		self.ur = hxs.xpath("//div[@class='blocks pagin listingbarbtm']/div[@class='fr']/div[@class='fl']/ul/li/a/@href").extract()
		event = hxs.xpath("//div[@class='tabsdatabox']/div[@class='tabsdatalft rightvsep fl']/ul[@class='tabsdataboxlists fl']/li[@class='mb6']/h5/a/span/text()").extract()
		date = hxs.xpath("//div[@class='tabsdatabox']/div[@class='tabsdatatkt fl']/p[@class='calndricon b']/text()").extract()
		place = hxs.xpath("//div[@class='tabsdatabox']/div[@class='tabsdatalft rightvsep fl']/ul[@class='tabsdataboxlists fl']/li[@class='venueicon mb3']/h6/a/text()").extract()
		place1 = hxs.xpath("//div[@class='tabsdatabox']/div[@class='tabsdatalft rightvsep fl']/ul[@class='tabsdataboxlists fl']/li[@class='areaicon']/span/text()").extract()
		type = hxs.xpath("//div[@class='tabsdatabox']/div[@class='tabsdatatkt fl']/p[@class='tagsicon']/span/text()").extract()
		#event.append(hxs.xpath("//div[@itemprop='events']/div[@class='tabsdatalft rightvsep fl']/ul[@class='tabsdataboxlists fl']/li[@class='mb6']/h5/a/span/text()").extract())
		#date.append(hxs.xpath("//div=[@itemprop='events']/div[@class='tabsdatatkt fl']/p[@class='calndricon b']/text()").extract())
		#place.append(hxs.xpath("//div=[@itemprop='events']/div[@class='tabsdatalft rightvsep fl']/ul[@class='tabsdataboxlists fl']/li[@class='venueicon mb3']/h6/a/text()").extract())
		#place1.append(hxs.xpath("//div=[@itemprop='events']/div[@class='tabsdatalft rightvsep fl']/ul[@class='tabsdataboxlists fl']/li[@class='areaicon']/span/text()").extract())
		#type.append(hxs.xpath("//div=[@itemprop='events']/div[@class='tabsdatatkt fl']/p[@class='tagsicon']/span/text()").extract())
		#print date
		time = []
		l=len(event)
		for i in range(l):
			self.c.writerow([event[i],type[i],place[i],place1[i],date[i],""])
		'''#print self.ur
		print event
		#print len(event)
		print
		print place
		#print len(place)
		print
		print place1
		#print len(place1)
		print
		print date
		#print len(date)'''
		for i in range(1,len(self.ur)):
			yield scrapy.http.Request(self.ur[i],callback = self.parse1)
			
	def parse1(self,response):
		hxs = Selector(response)
		#self.ur = hxs.xpath("//div[@class='blocks pagin listingbarbtm']/div[@class='fr']/div[@class='fl']/ul/li/a/@href").extract()
		event = hxs.xpath("//div[@class='tabsdatabox']/div[@class='tabsdatalft rightvsep fl']/ul[@class='tabsdataboxlists fl']/li[@class='mb6']/h5/a/span/text()").extract()
		date = hxs.xpath("//div[@class='tabsdatabox']/div[@class='tabsdatatkt fl']/p[@class='calndricon b']/text()").extract()
		place = hxs.xpath("//div[@class='tabsdatabox']/div[@class='tabsdatalft rightvsep fl']/ul[@class='tabsdataboxlists fl']/li[@class='venueicon mb3']/h6/a/text()").extract()
		place1 = hxs.xpath("//div[@class='tabsdatabox']/div[@class='tabsdatalft rightvsep fl']/ul[@class='tabsdataboxlists fl']/li[@class='areaicon']/span/text()").extract()
		type = hxs.xpath("//div[@class='tabsdatabox']/div[@class='tabsdatatkt fl']/p[@class='tagsicon']/span/text()").extract()
		time = []
		l=len(event)
		for i in range(l):
			self.c.writerow([event[i],type[i],place[i],place1[i],date[i],""])
			
class MySpider10(BaseSpider):
	name = "MySpider10"
	allowed_domain = ["www.bookmyshow.com"]
	start_urls = ["http://in.bookmyshow.com/bangalore/sport"]
	#c = csv.writer(open("event.csv", "ab"))
	
	def parse(self,response):
		hxs = Selector(response)
		event = hxs.select("//div[@id='Box']/div[@id='InnerBox_1']/div[@class='list fleft']/div[@class='det fleft']/ul/li[@class='listhd']/a/text()]").extract()
		place = hxs.select("//div[@class='list fleft']/div[@class='det fleft']/ul/li/span[@class='bold']/text()").extract()
		date = hxs.select("//div[@class='list fleft']/div[@class='evdate fleft']/div[@class='dtblock']/span[@class='bold fnt14']/text()").extract()
		type = ["Sports",]
		place1 = ["Bangalore",]
		time = []
		event = []
		#ur = []
		print date
		print event
		print place
		#items=[]
		#l=len(event)
		#for i in range(l):
		#	self.c.writerow([event[i],type[0],place[i],place1[0],date[i],""])