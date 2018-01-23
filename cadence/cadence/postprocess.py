# -*- coding: utf-8 -*-
import csv

class PostProcesser(object):
    def __init__(self, database, table_name):
        self.database = database
        self.table_name = table_name

    def process(self):
        columns = ['URL',
                   'Name',
                   'UserName',
                   'Alliance',
                   'Region',
                   'MilSize',
                   'MilTech',
                   'MilTrain',
                   'GDP',
                   'Airforce',
                   'LastOnline',
                   'Alignment',
                   'EcoSys',
                   'Industry',
                   'RMProd',
                   'OilProd',
                   'Uranium',
                   'NukeReactor',
                   'Reputation',
                   'Territory']

        query_1 = '''SELECT {} FROM nations \
                ORDER BY Region ASC, MilSize DESC, MilTech DESC, \
                GDP DESC'''.format(', '.join(columns))

        query_2 = '''SELECT Region, Alliance, sum(MilSize) as Strength \
                    from nations where LastOnline <= 72 \
                    group by Alliance, Region \
                    order by Region asc, Strength desc'''

        with open('raw_output.csv', 'w+b') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(columns)
            for row in self.database.execute(query_1):
                writer.writerow([unicode(s).encode('utf_8') for s in row])

        with open('filtered_output.csv', 'w+b') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(('Region', 'Alliance', 'Strength'))
            for row in self.database.execute(query_2):
                writer.writerow([unicode(s).encode('utf_8') for s in row])