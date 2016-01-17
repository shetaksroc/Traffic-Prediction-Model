# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item, Field


class TimescityItem(Item):
	date = Field()
	event = Field()
	type = Field()
	place = Field()
	place1 = Field()
	time = Field()
