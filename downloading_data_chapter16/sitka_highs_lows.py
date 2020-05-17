import csv
from datetime import datetime

import matplotlib.pyplot as plt

# we are try to read comma separate values files.
filename = 'data/sitka_weather_2018_simple.csv'
with open(filename) as f:
    read = csv.reader(f)
    header = next(read)
    # header1 = next(read)
    print(header)
    # print(header1)

    for index, column_reader in enumerate(header):
        # index += 1
        print(index, column_reader)

    # Get dates and  high temperatures from the file.
    dates, highs, lows = [], [], []
    for row in read:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        high = int(row[5])
        low = int(row[6])

        dates.append(current_date)
        highs.append(high)
        lows.append(low)

    print(lows)
    print(highs)
    print(dates)

    # Plot the high temperatures.
    plt.style.use('seaborn')
    # fig, ax = plt.subplots(figsize=(20, 5), dpi=128)
    fig, ax = plt.subplots()

    # ax.scatter(dates, highs, s=10, c='green')
    # ax.scatter(dates, lows, s=10, c='brown')
    ax.plot(dates, highs, c='orange', alpha=0.5)
    ax.plot(dates, lows, c='red', alpha=0.5)
    plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

    # Format plot.
    plt.title('Daily high and low temperatures - 2018', fontsize=24)
    plt.xlabel('', fontsize=14)
    fig.autofmt_xdate()
    plt.ylabel('Temperature(F)', fontsize=14)

    plt.tick_params(axis='both', which='major', labelsize=16)

    # plt.ylim(40, 80)
    plt.show()
