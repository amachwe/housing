import numpy as np
import tensorflow as tf
from matplotlib import pyplot as plt
from matplotlib.dates import YearLocator, MonthLocator
import datetime as dt
import operator



def loc_date_price(data_file):
    mnth_yrs_geo_price_data = []
    
    for line in data_file:
        items = line.split(",")

        try:
            items = (float(items[1]),float(items[2]),int(items[5]),int(items[6]),int(items[4]))
            mnth_yrs_geo_price_data.append(items)
        except ValueError as ve:
            print(items)
    
    return mnth_yrs_geo_price_data


def postcode_date_price(data_file):
    mnth_yrs_postcode_price_data = []

    for line in data_file:
        items = line.split(",")

        try:
            date = dt.date(year=int(items[5]), month=int(items[6]), day=15)
            items = (items[0], date, int(items[4]))
            mnth_yrs_postcode_price_data.append(items)
        except ValueError as ve:
            print(ve,items)

    return mnth_yrs_postcode_price_data


def date_price(data_file):
    mnth_yrs_data = {}

    for line in data_file:
        items = line.split(",")

        try:
            key = dt.date(year=int(items[5]), month=int(items[6]),day=15)
            value = float(items[4])

            if key in mnth_yrs_data:
                mnth_yrs_data[key] = (mnth_yrs_data[key][0] + value, mnth_yrs_data[key][1] + 1)
            else:
                mnth_yrs_data[key] = (value, 1)

        except ValueError as ve:
            print(line)
            print(items)

    return sorted(mnth_yrs_data.items(),key=operator.itemgetter(0))
    

data_file = open("value_add_postcode_geo_yr_mn_price.csv",'r')

print("Loading")

raw_data = postcode_date_price(data_file)

data_file.close()

print("Loaded")

dates = []
prices = []
file = open("postcode_prices_time.txt", 'w')
for data in raw_data:
    #date = data[0];
    #avg_price = data[1][0]/data[1][1]
    #dates.append(date)
    #prices.append(avg_price)

    date = data[1]
    postcode = data[0]
    avg_price = data[2]

    file.write(str(postcode)+","+str(date.year) +"," + str(date.month) + "," + str(avg_price)+"\n")


file.close()

#plt.plot_date(dates, prices, '-')
#plt.show()