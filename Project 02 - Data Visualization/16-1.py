import csv
from datetime import datetime
from matplotlib import pyplot as plt

filename = 'data/sitka_weather_2018_simple.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    # for index, column_header in enumerate(header_row):
    #     print(index, column_header)

    dates, prcps = [], []
    for row in reader:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        dates.append(current_date)
        prcp = float(row[3])
        prcps.append(prcp)

plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(dates, prcps, c='blue')

plt.title("Daily Precipitation - 2018", fontsize=24)
plt.xlabel('', fontsize=16)
fig.autofmt_xdate()
plt.ylabel("Inches of Rain", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)

plt.show()
