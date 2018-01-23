# -*- coding: utf-8 -*-

import scrapy
from scrapy.contrib.loader.processor import TakeFirst, MapCompose, Join

def MilTech_to_int(MilTech):
	MilTechLVL = {
	u'Advanced':u'9',
	u'Persian Gulf War surplus':u'8',
	u'Almost Modern':u'7',
	u'Vietnam War surplus':u'6',
	u'Korean War surplus':u'5',
	u'Second World War surplus':u'4',
	u'First World War surplus':u'3',
	u'Finest of the 19th century':u'2',
	u'Stone Age':u'1',
	}
	try:
		return MilTechLVL[MilTech]
	except KeyError:
		return u'1'

def MilTrain_to_int(MilTrain):
	MilTrainLVL = {
	u'Elite':u'5',
	u'Good':u'4',
	u'Standard':u'3',
	u'Poor':u'2',
	u'Undisciplined Rabble':u'1'
	}
	try:
		return MilTrainLVL[MilTrain]
	except KeyError:
		return u'3'

class Nation(scrapy.Item):
    EcoSys = scrapy.Field()
    Industry = scrapy.Field()
    GDP = scrapy.Field()
    URL = scrapy.Field()
    Name = scrapy.Field()
    UserName = scrapy.Field()
    Alignment = scrapy.Field()
    Alliance = scrapy.Field()
    Region = scrapy.Field()
    MilSize = scrapy.Field()
    MilTrain = scrapy.Field(
    	output_processor=MapCompose(MilTrain_to_int)
    )
    MilTech = scrapy.Field(
    	output_processor=MapCompose(MilTech_to_int)
    )
    Airforce = scrapy.Field()
    Uranium = scrapy.Field()
    Territory = scrapy.Field()
    LastOnline = scrapy.Field()
    NukeReactor = scrapy.Field()
    OilProd = scrapy.Field()
    RMProd = scrapy.Field()
    Reputation = scrapy.Field()
