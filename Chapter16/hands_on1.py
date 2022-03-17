import csv
import matplotlib.pyplot as plt
from datetime import datetime

from numpy import double
filename = 'Chapter16/sanfran_temps2022.csv'

with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    #Get high temps
    dates, highs, lows = [], [], []
    for row in reader:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        #invalid literal for int() with base 10; I don't understand this error
        high = int(row[4])
        low = int(row[5])
        dates.append(current_date)
        highs.append(high)
        lows.append(low)


#Plot  temps
plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(dates, highs, c='darkorange')
ax.plot(dates, lows, c='lightblue')
ax.fill_between(dates, highs, lows, facecolor='green')

#Format
ax.set_title("Daily Temps for San Francisco, Q1 2022", fontsize=24)
ax.set_xlabel('', fontsize=16)
fig.autofmt_xdate()
ax.set_ylabel("Temperature (F)", fontsize=16)
ax.tick_params(axis='both', which='major', labelsize=16)

plt.show
