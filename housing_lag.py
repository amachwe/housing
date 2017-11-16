from matplotlib import pyplot as plt
from datetime import datetime as dt
from matplotlib.dates import YearLocator, MonthLocator, DateFormatter

data = open("housing_data_mnth_cnt_grp.csv", mode='r')

header = None
items = []
for line in data:
    if header is None:
        header = line.split(",")
        print(header)
        continue

    data = line.split(",")
    month = data[0]
    year = data[1]
    avg = float(data[2]*1)
    stdev = float(data[3]*1)
    count = int(data[4]*1)

    date = dt.strptime("15-"+month+str("-")+year, "%d-%m-%Y").date()

    item = {
        "date": date,
        "avg": avg,
        "count": count
    }

    items.append(item)

items.sort(key=lambda x: x["date"])

count_d = []
price_d = []
date_d = []

prev = None
skip = 3

for it in items:
    count_d.append(it["count"])
    price_d.append(it["avg"])
    date_d.append(it["date"])

x = []
y = []

c = 0
for i in range(0,len(count_d),skip):
    temp_count = 0
    temp_price = 0
    for c in range(0,skip):
        if i+c < len(count_d):
            temp_count += count_d[i+c]
            temp_price += price_d[i+c]
    x.append(temp_count/skip)
    y.append(temp_price/skip)




print(len(count_d),len(count_d)/skip,len(x))
# plt.scatter(x,y)

x_ = []
y_ = []
end_block = 1

for i in range(0,len(x)):
    x_.append(x[i])
    y_.append(y[i])
# for i in range(1,len(x)-end_block):
#     x_.append(x[i-1])
#     y_.append((-y[i-1]+y[i])/x[i-1])

plt.scatter(x_,y_,s=8)
#plt.gca().xaxis.set_minor_locator(MonthLocator())
#plt.scatter(x,y,s=3)
plt.show()

print(y_,"\n",x_,"\n",price_d)


