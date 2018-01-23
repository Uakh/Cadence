#! /usr/bin/env python
#CODEDOT 2014
#v0.0.1
#Pre-Alpha
#MotD: "You never go full CGL"

import sqlite3
import urllib
import CODEpageparse

dbconnect = sqlite3.connect('cache.db')
dbc = dbconnect.cursor()

def CreateNewCache():
	dbc.execute('DROP TABLE nations')
	dbc.execute('CREATE TABLE nations (id, name)')
	dbconnect.commit()

def ParseNationPage(adress):
	q = urllib.parse.urlparse(adress)
	q = urllib.parse.parse_qs(q.query)
	nation = (q.id,)
	dbc.execute('INSERT INTO nations VALUES (?,?)', nation)