# -*- coding: utf-8 -*-
from scrapy.contrib.exporter import BaseItemExporter

class SQLItemExporter(BaseItemExporter):
    def __init__(self, database, table_name, **kwargs):
        super(self.__class__, self).__init__(**kwargs)
        self.database = database
        self.table_name = table_name
        self._initialized = False

    def export_item(self, item):
        if not self._initialized:
            self._initialize(item)
            self._initialized = True
        values = self._list_to_string(item)
        value_args = []
        for i in values:
            value_args.append('?')
        value_args = ', '.join(value_args)
        query = 'INSERT INTO {} ({}) VALUES ({})'.format(self.table_name, ', '.join(values.keys()), value_args)
        self.database.execute(query, values.values())
        self.database.commit()

    def _initialize(self, item):
        self.database.execute('DROP TABLE IF EXISTS {}'.format(self.table_name))
        if not self.fields_to_export:
            self.fields_to_export = item.fields.keys()
        columns = []
        for field in self.fields_to_export:
            columns.append(' '.join((field, 'NUMERIC')))
        self.database.execute('CREATE TABLE {} ({})'.format(self.table_name, ', '.join(columns)))
        #commit() is implied by CREATE

    def _list_to_string(self, item):
        stringified = dict(item)
        for i in stringified.keys():
            if isinstance(stringified[i], list):
                stringified[i] = stringified[i][0]
        return stringified