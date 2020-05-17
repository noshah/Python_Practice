import csv
from datetime import datetime

import matplotlib.pyplot as plt


filename = 'data/sitka_weather_2018_simple.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header = next(reader)
    print(header)
    rainfalls, dates = [], []
    for row in reader:
        current_dates = datetime.strptime(row[2], '%Y-%m-%d')
        rainfall = float(row[3])
        dates.append(current_dates)
        rainfalls.append(rainfall)
    print(dates)
    print(rainfalls)

    plt.style.use('seaborn')
    fig, ax = plt.subplots()
    ax.plot(dates, rainfalls, c='lightblue')

    # fill the label.
    title = 'Daily high and low rainfalls - 2018'
    plt.title(title, fontsize=20)
    plt.xlabel('', fontsize=14)
    plt.ylabel('Rainfalls Each Day Values', fontsize=14)
    fig.autofmt_xdate()

    plt.tick_params(axis='both', which='major', labelsize=16)
    plt.show()
