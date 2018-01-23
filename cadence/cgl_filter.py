#! /usr/bin/env python

import csv

def main():
    with open('blocgame_nations.csv', 'rb') as csvfile_input:
        with open('filtered_nations.csv', 'w+b') as csvfile_output:
            nation_reader = csv.DictReader(csvfile_input)
            columns = nation_reader.fieldnames
            nation_writer = csv.DictWriter(csvfile_output, columns)
            nation_writer.writeheader()
            for nation in nation_reader:
                if item_filter(nation):
                    nation_writer.writerow(nation)

def item_filter(nation):
    if (nation['Region'] in ('Amazonia',
                             'Caribbean',
                             'Mesoamerica',
                             'Gran Colombia',
                             'Southern Cone')
    and int(nation['GDP'])>=300
    and nation['Alliance'] in ('Che Guevara League',
                               'CGFL',
                               'BAMF',
                               'The Federal Colonies',
                               'New Lunar Republic',
                               'The Bronto Fanclub',
                               'UFN',
                               'The Sealion League',
                               'The Cartel',
                               'JIDF',
                               'Comintern')):
        return True
    else:
        return False

main()