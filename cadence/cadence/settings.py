# -*- coding: utf-8 -*-

# Scrapy settings for cadence project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'cadence'

SPIDER_MODULES = ['cadence.spiders']
NEWSPIDER_MODULE = 'cadence.spiders'
ITEM_PIPELINES = {
	'cadence.pipelines.SQLPipeline': 666,
	#'cadence.pipelines.CSVPipeline': 667,
    'cadence.pipelines.PostProcessPipeline': 999,
}
#Personnal settings below
DATABASE_EXPORT_FILENAME = 'nations.db'
DATABASE_EXPORT_TABLE = 'nations'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
USER_AGENT = 'CadenceBot'
