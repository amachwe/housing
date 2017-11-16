from gdp_processor import InflationValue
import csv
import collections
from datetime import datetime as dt
from multiprocessing import Pool
from contextlib import closing




def get_date(str_date):
    '''Date format expected - YYYY-MM-DD <TIME>'''
    str_date, str_time = str_date.split(" ")
    year, month, day = str_date.split("-")
    return dt(int(year),int(month),int(day))


def process_line(line):

    date = get_date(line[2])
    address = line[3]+" "+ line[7]+" "+line[9]+" "+line[11]
    price = line[1]
    if date >= inf.get_start_date():
        if data.get(address) is None:
            data[address] = collections.OrderedDict({})

        data[address][date] = price


housing = open("c:\\ml stats\\aug_17_housing.csv",mode='r')


inf = InflationValue()
data = {}

print "Exceute"
if __name__ == '__main__':

    with closing(Pool(processes=2)) as procs:
        procs.map( process_line,csv.reader(housing))
    print(data)

