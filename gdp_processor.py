import csv
from datetime import datetime as dt
import collections

class InflationValue(object):

    def __init__(self):
        cpi = open("c:\\ml stats\\cpi gbr.csv",mode='r')

        data = {}
        for line in csv.reader(cpi):
            if line[0] == "GBR":
                year, month = line[5].split("-")

                data[dt(int(year),int(month),1,0)] = float(line[6])

        ordered = collections.OrderedDict(sorted(data.items()))

        self.lookup = collections.OrderedDict({})
        self.end_date =  None
        self.start_date = None

        for key1 in ordered.keys():

            self.lookup[key1] = {}
            inflation = 1

            for key2 in ordered.keys():

                if key2 > key1:
                    inflation = inflation * (1 + (ordered.get(key2) / 100))
                    self.lookup[key1][key2] = inflation

    def get_value(self,start_year,start_month,end_year,end_month):
        '''Give equivalent value of 1 GBP at end date'''

        start_date = dt(int(start_year),int(start_month),1,0)
        end_date = dt(int(end_year),int(end_month),1,0)

        temp = self.lookup.get(start_date)
        if temp is not None:
            return temp.get(end_date)

        return temp

    def get_start_date(self):
        if self.start_date is None:
            self.start_date = self.lookup.keys()[0]
        return self.start_date

    def get_end_date(self):
        if self.end_date is None:
            self.end_date = self.lookup.keys()[-1]
        return self.end_date


