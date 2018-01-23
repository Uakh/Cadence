from scrapy.contrib.loader import ItemLoader
from scrapy.contrib.loader.processor import TakeFirst, MapCompose, Join

class NationLoader(ItemLoader):
	default_output_processor = TakeFirst()