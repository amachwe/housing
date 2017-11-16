import tensorflow as tf
import datetime as dt
import math
import random
import numpy as np

from matplotlib import pyplot as plt

MAX_SAMPLE = 10000

file = open("prices_time.txt", "r")

dates = []
prices = []
for line in file:
    items = line.split(",")
    dates.append((items[0], items[1]))
    prices.append(float(items[2]))

plt.plot(prices)
plt.show()


total = len(dates)
rets_perct = []
rets_annual = []
durs_mnths = []

durs_rets_dict = {}
durs_rets_annual_dict = {}


while MAX_SAMPLE>0:

    j = random.randint(0, total-2)
    k = random.randint(j+1, total-1)

    period_mnths = (k - j)
    period_yrs = math.ceil(period_mnths/12.0)
    durs_mnths.append(period_mnths)

    ret = (prices[k] - prices[j]) / prices[j]
    ret_annual = ((1+ret)**(1/period_yrs) - 1)
    rets_perct.append(ret * 100)

    MAX_SAMPLE -= 1

    durs_rets_annual_dict.setdefault(period_yrs, []).append(ret_annual)
    durs_rets_dict.setdefault(period_mnths, []).append(ret)

plt.plot(durs_mnths, rets_perct, '.',ms=2)
plt.grid(True)
plt.show()

stds = []
avgs = []
for durs in durs_rets_annual_dict.keys():
    stds.append(np.std(durs_rets_annual_dict[durs]))
    avgs.append(np.average(durs_rets_annual_dict[durs]))

plt.errorbar(durs_rets_annual_dict.keys(), avgs, yerr=stds, fmt=".")
plt.grid(True)
plt.show()

#plt.plot(durs_rets_dict.keys(), avgs, '.',ms= 4)
#plt.grid(True)
#plt.show()

#X0 = tf.placeholder(tf.float32,9)
