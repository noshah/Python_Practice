import csv
from datetime import datetime

import matplotlib.pyplot as plt

filname='data/2152057.csv'
with open(filname) as f:
    reader = csv.reader(f)
    header = next(reader)
    print(header)

    for index, name in enumerate(header):
        print(index, name)

    rains, dates = [], []
    for row in reader:
        date = datetime.strptime(row[2], '%Y-%m-%d')
        try:
            rain = float(row[5])
        except ValueError:
            print(f'Missing data for {date}.')
        else:
            dates.append(date)
            rains.append(rain)
    print(dates)
    print(rains)

    plt.style.use('seaborn')
    fig, ax = plt.subplots()
    ax.plot(dates, rains, c='green')

    title = 'San Francisco daily Precipitation \n 2019-2020'
    plt.title(title, fontsize=20)
    plt.xlabel('', fontsize=14)
    plt.ylabel('Precipitation of rain', fontsize=14)
    fig.autofmt_xdate()
    plt.tick_params(axis='both', which='major', labelsize=18)

    plt.show()
