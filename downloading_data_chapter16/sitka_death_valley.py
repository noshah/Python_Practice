import csv
from datetime import datetime

import matplotlib.pyplot as plt

# we are try to read comma separate values files.
filename = 'data/sitka_weather_2018_simple.csv'
filename_1 = 'data/death_valley_2018_simple.csv'

with open(filename) as f:
    read = csv.reader(f)
    header = next(read)
    # header1 = next(read)
    print(header)
    # print(header1)


    for index, column_reader in enumerate(header):
        # index += 1
        print(index, column_reader)

    # Get High Temperature and Dates.
    highs, dates = [], []
    for row in read:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        high = int(row[5])

        dates.append(current_date)
        highs.append(high)

with open(filename_1) as f:
    reader = csv.reader(f)
    header_1 = next(reader)
    # header1 = next(read)
    print(header_1)
    # print(header1)

    highs_1, dates_1 = [], []
    for row in reader:
        date = datetime.strptime(row[2], '%Y-%m-%d')
        try:
            high_1 = int(row[4])
        except ValueError:
            print(f"Missing data for {date}")
        else:
            dates_1.append(date)
            highs_1.append(high_1)
    print(highs_1)
    print(highs)
    # Plot the high temperatures.
    plt.style.use('seaborn')
    # fig, ax = plt.subplots(figsize=(20, 5), dpi=128)
    fig, ax = plt.subplots()

    # ax.scatter(dates, highs, s=20, c='green')
    # ax.scatter(dates_1, highs_1, s=20, c='green')
    ax.plot(dates, highs, c='orange', alpha=0.5)
    ax.plot(dates_1, highs_1, c='red', alpha=0.5)
    plt.fill_between(dates, highs, highs_1, facecolor='red', alpha=0.1)
    # Format plot.
    plt.title('Daily high temperatures\n for Sitka and Death_Vallay - 2018', fontsize=20)
    plt.xlabel('', fontsize=14)
    fig.autofmt_xdate()
    plt.ylabel('Temperature(F)', fontsize=14)

    plt.tick_params(axis='both', which='major', labelsize=16)

    # plt.ylim(40, 80)
    plt.show()

