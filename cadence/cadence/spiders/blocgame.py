# -*- coding: utf-8 -*-
import scrapy
import string
from cadence.itemloaders import NationLoader
from cadence.items import Nation


class BlocgameSpider(scrapy.Spider):
    name = "blocgame"
    allowed_domains = ["blocgame.com"]
    start_urls = (
        'http://blocgame.com/rankings.php',
    )

    def parse(self, response):
        for href in response.xpath('//h4/a/@href').extract():
        	yield scrapy.Request(self.internal_href(href), callback=self.parse_nation)

        for href in response.xpath('//ul[@class="pagination"]//@href').extract():
        	yield scrapy.Request(self.internal_href(href), callback=self.parse)

    def parse_nation(self, response):
    	eco_offset, ura_offset = 0, 0
    	l = NationLoader(item=Nation(), response=response)
    	l.add_value('URL', response.url)
    	#Have to use an offset in case of foreign investments or uranium
    	if l.get_xpath('//div[@id="collapseThree"]//tr[5]/td[1]/text()') == [u'Foreign Investment:']:
    		eco_offset += 1
        #And uranium offset in case someone has both uranium and a nuke somehow
        if l.get_xpath(string.join(('//div[@id="collapseThree"]//tr[',
                        str(10+eco_offset), ']/td[1]/text()'), '')) == [u'Uranium:']:
            ura_offset += 1
    	l.add_xpath('EcoSys', '//div[@id="collapseThree"]//tr[1]/td[2]/i/text()')
    	l.add_xpath('Industry', '//div[@id="collapseThree"]//tr[2]/td[2]/i', re='[0-9]+')
        l.add_value('Industry', u'0')
    	l.add_xpath('GDP', '//div[@id="collapseThree"]//tr[3]/td[2]/i/text()', re='[0-9]+')
    	l.add_xpath('Uranium', string.join(('//div[@id="collapseThree"]//tr[', str(10+eco_offset), ']/td[2]/i/text()'), ''), re='[0-9]+')
    	l.add_value('Uranium', u'0')
    	l.add_xpath('Name', '//p[@id="nationtitle"]/b/text()')
    	l.add_xpath('UserName','//i[@class="lead"][2]/b//text()')
    	l.add_xpath('Alignment', '//div[@id="collapseFour"]//tr[1]/td[2]/i/text()')
    	l.add_xpath('Region', '//div[@id="collapseFour"]//tr[2]/td[2]/i/a/text()')
    	l.add_xpath('Alliance', '//div[@id="collapseFour"]//tr[3]/td[2]/i//text()')
    	l.add_xpath('MilSize', '//div[@id="collapseFive"]//tr[1]/td[2]/i/text()', re='[0-9]+')
    	l.add_xpath('MilTech', '//div[@id="collapseFive"]//tr[3]/td[2]/i/text()')
    	l.add_xpath('MilTrain', '//div[@id="collapseFive"]//tr[5]/td[2]/i/text()')
    	l.add_xpath('Airforce', '//div[@id="collapseFive"]//tr[6]/td[2]/i/text()')
    	l.add_xpath('Territory', '//div[@id="collapseTwo"]//tr[4]/td[2]/i/text()', re='[0-9]+')
    	#The line below is the XPath you'd think is right but your browser will LIE to you,
    	#the </center> tag is misplaced which fucks up the <div>. Yes we checked on several rigs.
    	#See for yourself with //div[@id="accordion2"]/div/div (and no regex you potato)
    	#l.add_xpath('LastOnline', '//div[@id="accordion2"]//center/font[@size="2"]/text()', re='[0-9]+')
    	l.add_xpath('LastOnline', '//div[@id="accordion2"]/div/div/font[@size=2]/text()', re='[0-9]+')
    	l.add_value('LastOnline', u'0')
    	l.add_xpath('NukeReactor',string.join(('//div[@id="collapseThree"]//tr[', str(10+eco_offset+ura_offset), ']/td[2]/i/div/div/@style'), ''), re='[0-9]+')
    	l.add_value('NukeReactor', u'0')
        l.add_xpath('OilProd', string.join(('//div[@id="collapseThree"]//tr[', str(6+eco_offset), ']/td[2]/i/text()'), ''), re='[0-9]+')
        l.add_value('OilProd', u'0')
        l.add_xpath('RMProd', string.join(('//div[@id="collapseThree"]//tr[', str(8+eco_offset), ']/td[2]/i/text()'), ''), re='[0-9]+')
        l.add_xpath('Reputation', '//div[@id="collapseFour"]//tr[4]/td[2]/i//text()')
    	return l.load_item()

    def internal_href(self, href):
    	return string.join(('http://www.blocgame.com/', href), '')