#! /usr/bin/env python

import urllib
from html.parser import HTMLParser

class NationPageParser(HTMLParser):

def parseNationPage(adress):
	parser = NationPageParser()
	stream = urllib.request.urlopen(adress)
	parser.feed(stream.read())