# -*- coding: utf-8 -*-
import sqlite3
from scrapy.contrib.exporter import CsvItemExporter
from cadence.sql import SQLItemExporter
from cadence.postprocess import PostProcesser
from cadence import settings

class SQLPipeline(object):
    def process_item(self, item, spider):
        self.exporter.export_item(item)
        return item
    def open_spider(self, spider):
        filename = settings.DATABASE_EXPORT_FILENAME
        table = settings.DATABASE_EXPORT_TABLE
    	self.dbconnect = sqlite3.connect(filename)
        self.exporter = SQLItemExporter(self.dbconnect, table)
   	def close_spider(self, spider):
   		self.dbconnect.close()

class CSVPipeline(object):
    def __init__(self):
        self.files = {}

    def process_item(self, item, spider):
        self.exporter.export_item(item)
        return item
    def open_spider(self, spider):
        file = open('%s_nations.csv' % spider.name, 'w+b')
        self.files[spider] = file
        self.exporter = CsvItemExporter(file)
        self.exporter.start_exporting()
    def close_spider(self, spider):
        self.exporter.finish_exporting()
        file = self.files.pop(spider)
        file.close()

class PostProcessPipeline(object):
    def process_item(self, item, spider):
        return item
    def open_spider(self, spider):
        filename = settings.DATABASE_EXPORT_FILENAME
        table = settings.DATABASE_EXPORT_TABLE
        self.dbconnect = sqlite3.connect(filename)
        self.exporter = PostProcesser(self.dbconnect, filename)
    def close_spider(self, spider):
        self.exporter.process()
        self.dbconnect.close()